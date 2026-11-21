# x402: universal primitives, repurposed for the WET-112 wiki

Ticket: [NS001-158](https://linear.app/mchu001/issue/NS001-158/get-universal-primitives-x402), written for [WET-112](https://linear.app/mchu001/issue/WET-112/create-open-source-wiki).
Rule: [MCHU-91](https://linear.app/mchu001/issue/MCHU-91/engineering-principles) (minimum idiot index, maximum clinical utility).
Style: [MCHU-103](https://linear.app/mchu001/issue/MCHU-103/learn-the-fundamentals) (0.25 first principles, 0.25 brute fact, 0.5 abstraction).
Upstream pin: `x402-foundation/x402@ad9a38fdd1800641d17fc73a947156471265fef2`, retrieved 2026-11-21 (`data/pins.json`).
Scope: academic study. Nothing here moves funds, gives payment instructions or makes a clinical recommendation. A passing check proves shape, not truth.

```sh
cd x402
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/python scripts/retrieve.py   # re-pin sources, refresh live fixtures in data/
.venv/bin/python scripts/validate.py   # exit 0 = all checks and red-team mutants pass
```

---

## 1. First principles (0.25)

1. A resource on a network can refuse service until a condition is met. HTTP has reserved status `402 Payment Required` for this since 1997, but never defined how to state the condition. x402 defines it.
2. The condition must be machine-readable, so an agent with no account and no human can meet it. x402 makes it a JSON object.
3. Whoever meets the condition must prove it without the server trusting them. x402 uses a signature over the exact terms, checked by a third party.
4. The proof must be single-use and time-limited, or it can be replayed. x402 uses a nonce and a validity window.
5. The outcome must be recorded somewhere neither party controls. x402 settles on a public chain and returns the transaction hash.

Remove "payment" from these five and what is left is general: **state a condition, prove it with a signature, check it independently, record the result.** A wiki that agents write to needs the same five things for every claim.

## 2. Brute facts (0.25)

Each row: claim, pinned locus, read status. `claim-checked` = read at the pin or confirmed by `validate.py`.

| # | Fact | Locus | Status |
|---|---|---|---|
| 1 | Three roles: client, resource server, facilitator. The facilitator handles verification and chain settlement. | spec-v2 §3 | claim-checked |
| 2 | Cycle: request → `402` + `PaymentRequired` → retry with `PaymentPayload` → `/verify` → serve → `/settle` → `SettlementResponse`. | spec-v2 §2 | claim-checked |
| 3 | `PaymentRequired` = `{x402Version: 2, error?, resource, accepts[1..1024], extensions?}`. | TS `schemas/index.ts`; Py `schemas/payments.py` | claim-checked |
| 4 | `PaymentRequirements` = `{scheme, network, amount, asset, payTo, maxTimeoutSeconds, extra}`. `amount` is a string in the asset's smallest unit. | same | claim-checked |
| 5 | `PaymentPayload` = `{x402Version, resource?, accepted, payload, extensions?}`. `accepted` echoes one entry of `accepts`. `payload` is scheme-specific. | spec-v2 §5.2 | claim-checked |
| 6 | `network` must match `^[-a-z0-9]{3,8}:[-_a-zA-Z0-9]{1,32}$` (CAIP-2 `namespace:reference`). TS and Python SDKs enforce the same regex. | TS + Py schemas | claim-checked |
| 7 | Extensions are `{info, schema}`. The client "must include at least the info received; it may append additional info but cannot delete or overwrite existing info." | spec-v2 §5.1.2 | claim-checked |
| 8 | `/verify` is read-only and "MUST NOT commit payment state or write onchain state". `/settle` writes. | spec-v2 §7.1 | claim-checked |
| 9 | `SettleResponse` has `success`, `transaction`, `network` (required) and `payer`, `amount`, `errorReason`, `extensions` (optional). `settlement_pending` requires a non-empty `transaction`. | spec-v2 §5.3 | claim-checked |
| 10 | Clients must match on `invalidReason` / `errorReason` codes, never on message text. | spec-v2 §9 | claim-checked |
| 11 | Replay protection: 32-byte nonce, validity window, payer signature, contract-level nonce reuse check (EIP-3009). | spec-v2 §10.1 | claim-checked |
| 12 | Schemes: `exact`, `upto`, `batch-settlement`, `auth-capture`. Payment flows: `authorization`, `upfront`, `escrow`. | spec-v2 §6, `specs/schemes/` | claim-checked |
| 13 | Transports specified: HTTP, MCP, A2A. HTTP v2 uses Base64 JSON headers `PAYMENT-REQUIRED`, `PAYMENT-SIGNATURE`, `PAYMENT-RESPONSE`. | `specs/transports-v2/` | claim-checked |
| 14 | `payment-identifier` extension: client-supplied `id` used as an idempotency key. | `extensions/payment_identifier.md` | claim-checked |
| 15 | `offer-and-receipt` extension: server signs the terms it offers and the receipt after delivery, for audit and reputation. | `extensions/extension-offer-and-receipt.md` | claim-checked |
| 16 | Live `x402.org/facilitator/supported` (testnet): 9 v2 kinds (7 `exact`, 1 `upto`, 1 `batch-settlement`) on 7 chains (EVM, Solana, Algorand, Aptos, Stellar, Hedera, XRPL) and 2 v1 kinds. | `data/supported.json` | claim-checked |
| 17 | Live CDP discovery: 38,469 listed resources. The 20 sampled items gave 33 valid requirements and 22 `{info, schema}` extensions. | `data/discovery.json` | claim-checked |
| 18 | One live extension (`agentkit`, Sign-In-With-X style) has `info` that **fails its own schema**: `address`, `signature`, `chainId` are missing. The schema describes the object the client completes, not the server's offer. | `data/discovery.json` | claim-checked |
| 19 | The CAIP-2 regex accepts `uniprot:P00533`, `pdb:1M17`, `hgnc:3236`, `chebi:15377`, `pmid:12748304`, `ensembl:ENSG00000146648`. It rejects `aa:ACD` (namespace < 3 chars), `doi:10.1038/...` (`/` and `.`) and `UniProt:` (uppercase). | `validate.py` | claim-checked |

Fact 18 corrects a naive validator. Fact 19 is why section 3 works.

## 3. Abstraction (0.5): x402 primitives as wiki primitives

### 3.1 The mapping

x402 is a protocol for *conditional access to a named resource, with signed, independently checked and permanently recorded outcomes*. Payment is one condition. In WET-112 the conditions are "a claim is pinned" and "a claim is verified". Every x402 object then has a wiki use without changing its shape.

| x402 primitive | WET-112 wiki primitive | Molecular-biology reading (analogy only) |
|---|---|---|
| CAIP-2 `namespace:reference` | **Page ID**: `uniprot:P00533`, `pdb:1M17`, `hgnc:3236`. The same regex validates chains and molecules. | Accession number |
| `ResourceInfo` `{url, description, mimeType, serviceName, tags≤5}` | **Page header**: `url = wiki://<page-id>`, `mimeType = text/markdown`, `tags` = entity type and read status | Locus annotation |
| `PaymentRequired` (402) | **Contribution terms**: what an agent must supply to read or edit the page | Receptor exposing a binding site |
| `accepts[]` | **Accepted proof paths**: one or more `scheme × network` ways to satisfy the terms | Allowed ligands |
| `PaymentRequirements.payTo` / `amount` | **Steward and stake**: who maintains the page and what an edit costs (optional; `0` = free) | Activation energy |
| `extensions.<key> = {info, schema}` | **Typed page body**: claims, pins, typed edges and content hash as `info`, with the JSON Schema it must satisfy | Domain fold with a defined shape |
| Add-only echo rule (fact 7) | **Append-only edits**: a contribution may add claims or edges but never delete or overwrite them. Same law as catalog's add-only relations. | Semi-conservative replication |
| `PaymentPayload.accepted` echo | **Binding**: an edit names the exact terms it answers, so nothing can be swapped underneath it | Codon–anticodon pairing |
| `payload` signature + nonce + validity window | **Signed, single-use contribution**: who wrote it, once, within a window | Single-turnover enzyme |
| Facilitator `/verify` (read-only) | **Verifier**: re-runs the pin (hash, locus, read status) without writing anything. Maps to WET-114's "named verifier". | Proofreading (exonuclease check) |
| `VerifyResponse.invalidReason` codes | **Refusal taxonomy**: machine codes such as `unpinned`, `hash_drift`, `overwrite`, never prose | Mismatch repair signal |
| Facilitator `/settle` | **Anchor**: write the page's content hash or Merkle root to a chain or IPFS (WET-81) | Ligation |
| `SettleResponse.transaction` / `settlement_pending` | **Anchor receipt** with a non-terminal pending state | Covalent mark |
| `/supported` `{kinds, extensions, signers}` | **Verifier registry**: which checks and anchors a verifier offers, and its public keys | Enzyme repertoire |
| Bazaar `/discovery/resources` | **Page index**: agents list and search pages by tag without crawling | Genome browser track |
| `payment-identifier` | **Edit idempotency key**: a repeated submission is not a second edit | — |
| `offer-and-receipt` | **Provenance receipts**: signed proof that an agent read version *h* of a page | Lab notebook countersignature |
| SIWX / CAIP-122 (fact 18) | **Contributor identity** without accounts | — |

### 3.2 The cycle, re-read

```
agent  GET wiki://uniprot:P00533
wiki   402  PaymentRequired{resource, accepts, extensions.wetware-page{info, schema}}
agent  PaymentPayload{accepted = accepts[i], payload = signed edit, extensions = info + appended claims}
wiki   → verifier /verify   (schema, add-only, hash, pin, read status; no writes)
wiki   200 page + PAYMENT-RESPONSE   → verifier /settle (anchor root) → receipt
```

`examples/wiki-page.json` is this exchange for `uniprot:P00533` (EGFR_HUMAN, UniProtKB entryVersion 302). `examples/uniprot-P00533.md` is the page body that `contentHash` pins. The example is unsigned and uses the Base Sepolia testnet; `payTo` is the zero address.

### 3.3 What carries over unchanged, and what does not

- **Reuse as-is:** CAIP-2 IDs, `ResourceInfo`, `PaymentRequired` / `PaymentPayload` envelopes, the `{info, schema}` extension slot and its add-only rule, the verify/settle split, reason codes, idempotency keys and receipts. The official SDK already validates the envelopes (`x402==2.29.0`), so the wiki writes no parser of its own.
- **Reuse, narrowed:** schemes and networks. A wiki needs at most one scheme (`exact`, amount `0` or a stake) and one anchor network. Ignore the other mechanism packages.
- **Do not reuse:** money-moving facilitators on mainnet. The public `x402.org` facilitator is for testnets only. Anchoring a hash does not require a payment.
- **ID gap:** the CAIP-2 shape cannot hold `doi:10.1038/...` or two-letter namespaces such as `aa:`. Route DOIs through `pmid:` or a hashed reference, and use namespaces of 3 or more characters (`aas:`, `dna:`).

### 3.4 Idiot index (MCHU-91)

Idiot index = cost of the finished part ÷ cost of its raw material. Here the raw material is already built and audited by others: schemas (SDK), IDs (CAIP-2), transport (HTTP 402) and anchoring (any chain). The wiki-specific code is three checks in `validate.py` (143 lines in total, mostly fixtures and mutants): add-only echo, content hash and claim schema. Anything larger is re-deriving x402.

Clinical utility comes from the claim layer (pin, locus, read status, verifier), not the payment layer. x402 only guarantees that a claim cannot be silently swapped, replayed or unattributed.

## 4. Red team (falsifiers in `validate.py`)

Each mutant must be **rejected**. All 8 are rejected at the pin.

| Mutant | Caught by |
|---|---|
| `network: base-sepolia` (v1 style) | SDK CAIP-2 validator |
| `accepted.amount` altered | echo binding |
| existing claim overwritten | add-only rule |
| claim without `pin` | page schema |
| `readStatus: trusted` | page schema enum |
| `contentHash` drift | body hash |
| page ID `doi:10.1038/x` | CAIP-2 shape |
| empty `accepts` | 1..1024 bound |

## 5. Limits

- Live fixtures drift. Re-run `retrieve.py` and re-pin rather than editing hashes.
- `validate.py` checks shape and binding. It does not verify signatures, call `/verify` or `/settle`, or check on-chain state.
- v1 kinds are counted separately and never validated as v2.
- The molecular-biology column is a teaching analogy, not a mechanism claim.
- Discovery data shows that a resource exists, not that it is safe or that it works.
