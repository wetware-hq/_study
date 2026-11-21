"""Retrieve pinned x402 sources and live public fixtures. Read-only: no wallet, no payment."""
import datetime
import hashlib
import json
import pathlib
import urllib.request

COMMIT = "ad9a38fdd1800641d17fc73a947156471265fef2"
RAW = f"https://raw.githubusercontent.com/x402-foundation/x402/{COMMIT}/"
SOURCES = [
    "specs/x402-specification-v2.md",
    "specs/transports-v2/http.md",
    "specs/extensions/payment_identifier.md",
    "specs/extensions/extension-offer-and-receipt.md",
    "typescript/packages/core/src/schemas/index.ts",
    "python/x402/schemas/payments.py",
]
LIVE = {
    "supported": "https://x402.org/facilitator/supported",
    "discovery": "https://api.cdp.coinbase.com/platform/v2/x402/discovery/resources?limit=5",
}
DATA = pathlib.Path(__file__).resolve().parent.parent / "data"


def get(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "wetware-study-x402"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()


def main() -> None:
    DATA.mkdir(exist_ok=True)
    now = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    pins = []
    for path in SOURCES:
        body = get(RAW + path)
        pins.append({"id": f"x402-foundation/x402@{COMMIT}:{path}", "retrieved": now,
                     "sha256": hashlib.sha256(body).hexdigest()})
    for name, url in LIVE.items():
        body = get(url)
        json.loads(body)
        (DATA / f"{name}.json").write_bytes(body)  # raw bytes, so sha256 below re-verifies offline
        pins.append({"id": url, "retrieved": now, "sha256": hashlib.sha256(body).hexdigest(),
                     "note": "live fixture; drifts; re-pin instead of repairing"})
    (DATA / "pins.json").write_text(json.dumps(pins, indent=2) + "\n")
    for p in pins:
        print(p["sha256"][:16], p["id"])


if __name__ == "__main__":
    main()
