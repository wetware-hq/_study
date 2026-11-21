"""Validate x402 v2 primitives (live fixtures) and their WET-112 wiki repurposing.

Uses the official x402 Python SDK models; adds only the checks the SDK leaves to callers.
Exit code 0 = every check and every red-team mutant behaved as expected.
"""
import copy
import hashlib
import json
import pathlib
import sys

import jsonschema
from pydantic import ValidationError
from x402.schemas import PaymentPayload, PaymentRequired, PaymentRequirements, SupportedKind
from x402.schemas.payments import _validate_caip2_network as caip2

ROOT = pathlib.Path(__file__).resolve().parent.parent
FAILS: list[str] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS " if ok else "FAIL ") + name + (f"  ({detail})" if detail else ""))
    if not ok:
        FAILS.append(name)


def is_caip2(value: str) -> bool:
    try:
        caip2(value)
        return True
    except ValueError:
        return False


def schema_errors(schema: dict, info: dict) -> list[jsonschema.ValidationError]:
    return list(jsonschema.Draft202012Validator(schema).iter_errors(info))


def add_only(server, client) -> bool:
    """Spec 5.1.2: client may append to extension info, never delete or overwrite."""
    if isinstance(server, dict):
        return isinstance(client, dict) and all(k in client and add_only(v, client[k]) for k, v in server.items())
    if isinstance(server, list):
        return isinstance(client, list) and len(client) >= len(server) and all(map(add_only, server, client))
    return server == client


def page_errors(page: dict) -> list[str]:
    errs = []
    offer, contrib = page["offer"], page["contribution"]
    try:
        req = PaymentRequired.model_validate(offer)
        pay = PaymentPayload.model_validate(contrib)
    except ValidationError as e:
        return [f"sdk: {e.errors()[0]['msg']}"]
    if not 1 <= len(req.accepts) <= 1024:
        errs.append("accepts must hold 1..1024 entries")
    tags = req.resource.tags or []
    if len(tags) > 5 or any(len(t) > 32 for t in tags):
        errs.append("resource.tags exceed bazaar limits")
    if pay.accepted not in req.accepts:
        errs.append("contribution.accepted is not an echo of offer.accepts")
    if pay.resource and pay.resource.url != req.resource.url:
        errs.append("contribution targets a different resource")
    for key, ext in (req.extensions or {}).items():
        got = (pay.extensions or {}).get(key, {})
        if not add_only(ext["info"], got.get("info")):
            errs.append(f"extension {key}: info deleted or overwritten")
        for e in schema_errors(ext["schema"], got.get("info") or {}):
            errs.append(f"extension {key}: {e.message}")
        page_id = ext["info"].get("id", "")
        if not is_caip2(page_id):
            errs.append(f"page id {page_id!r} is not namespace:reference")
        elif want := ext["info"].get("contentHash"):
            body = (ROOT / "examples" / f"{page_id.replace(':', '-')}.md").read_bytes()
            if want != "sha256:" + hashlib.sha256(body).hexdigest():
                errs.append("contentHash does not match page body")
    return errs


def live() -> None:
    sup = json.loads((ROOT / "data" / "supported.json").read_text())
    v2 = [k for k in sup["kinds"] if k["x402Version"] == 2]
    v1 = [k for k in sup["kinds"] if k["x402Version"] == 1]
    bad = [k["network"] for k in v2 if not is_caip2(SupportedKind.model_validate(k).network)]
    check("supported: v2 kinds parse, networks CAIP-2", not bad, f"{len(v2)} v2, {len(v1)} v1 kept apart; bad={bad}")
    check("supported: signer keys are namespace:* patterns",
          all(k.endswith(":*") and is_caip2(k[:-1] + "x") for k in sup.get("signers", {})))

    disc = json.loads((ROOT / "data" / "discovery.json").read_text())
    n_req = n_ext = n_partial = 0
    errs = []
    for item in disc["items"]:
        for a in item["accepts"]:
            try:
                PaymentRequirements.model_validate(a)
                n_req += 1
            except ValidationError as e:
                errs.append(f"{item['resource']}: {e.errors()[0]['msg']}")
        for key, ext in (item.get("extensions") or {}).items():
            if isinstance(ext, dict) and "info" in ext and "schema" in ext:
                n_ext += 1
                found = schema_errors(ext["schema"], ext["info"])
                # Server info may omit fields the client must add (spec 5.4 add-only echo).
                n_partial += bool(found)
                errs += [f"{item['resource']} {key}: {e.message}" for e in found if e.validator != "required"]
    check("discovery: accepts parse; extension info is schema-valid or awaits client fields", not errs,
          f"{len(disc['items'])} items, {n_req} requirements, {n_ext} extensions, {n_partial} await client fields; {errs[:3]}")


def identifiers() -> None:
    cases = {"uniprot:P00533": True, "pdb:1M17": True, "hgnc:3236": True, "chebi:15377": True,
             "pmid:12748304": True, "ensembl:ENSG00000146648": True,
             "aa:ACD": False, "doi:10.1038/nature01234": False, "UniProt:P00533": False}
    for value, want in cases.items():
        check(f"caip2 shape {value!r} -> {want}", is_caip2(value) is want)


def wiki() -> None:
    page = json.loads((ROOT / "examples" / "wiki-page.json").read_text())
    errs = page_errors(page)
    check("wiki page: offer/contribution are valid x402 v2 objects", not errs, "; ".join(errs))

    def mutant(name: str, edit) -> None:
        m = copy.deepcopy(page)
        edit(m)
        check(f"red team rejects: {name}", bool(page_errors(m)))

    ext = lambda m, side: m[side]["extensions"]["wetware-page"]["info"]

    def appended(m):
        ext(m, "contribution")["claims"].append(dict(ext(m, "contribution")["claims"][0], claim="EGFR gene symbol is EGFR"))
        ext(m, "contribution")["edges"].append({"type": "same_as", "to": "ensembl:ENSG00000146648"})
    m = copy.deepcopy(page)
    appended(m)
    errs = page_errors(m)
    check("wiki page: appended claim and edge are accepted", not errs, "; ".join(errs))
    mutant("non-CAIP-2 network", lambda m: m["offer"]["accepts"][0].update(network="base-sepolia"))
    mutant("accepted amount altered", lambda m: m["contribution"]["accepted"].update(amount="1"))
    mutant("claim overwritten", lambda m: ext(m, "contribution")["claims"][0].update(claim="EGFR is a kinase-dead receptor"))
    mutant("claim without pin", lambda m: [ext(m, s)["claims"][0].pop("pin") for s in ("offer", "contribution")])
    mutant("unknown read status", lambda m: [ext(m, s)["claims"][0].update(readStatus="trusted") for s in ("offer", "contribution")])
    mutant("content drift", lambda m: [ext(m, s).update(contentHash="sha256:" + "0" * 64) for s in ("offer", "contribution")])
    mutant("page id not namespace:reference", lambda m: [ext(m, s).update(id="doi:10.1038/x") for s in ("offer", "contribution")])
    mutant("empty accepts", lambda m: m["offer"].update(accepts=[]))


if __name__ == "__main__":
    live()
    identifiers()
    wiki()
    print(f"\n{len(FAILS)} failed" if FAILS else "\nall checks passed")
    sys.exit(1 if FAILS else 0)
