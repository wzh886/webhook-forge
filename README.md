# webhook-forge

**webhook-forge** is a developer-first toolkit for signing, verifying, replaying, and debugging webhook deliveries with minimal setup.

It is designed for engineers who build integrations and need a fast way to answer practical questions such as:
- Is this signature valid?
- What exact payload was signed?
- Can I replay this failed delivery locally?
- Why did this webhook consumer reject the event?

---

## Why this project matters
Webhook systems often fail at the seams:
- signature mismatches
- timestamp drift
- payload canonicalization bugs
- poor retry visibility
- hard-to-reproduce production failures

`webhook-forge` aims to reduce that friction by giving engineers a compact tool they can use during local development, testing, and incident response.

---

## Current capabilities
- HMAC-SHA256 payload signing
- signature verification helpers
- simple CLI commands for sign/verify flows
- minimal Python package structure for extension

### Current CLI
```bash
webhook-forge sign --secret whsec_test --timestamp 1712345678 --payload '{"ok":true}'
webhook-forge verify --secret whsec_test --timestamp 1712345678 --payload '{"ok":true}' --signature 'sha256=...'
```

---

## Installation
```bash
pip install -e .
```

Or run directly from source with:

```bash
PYTHONPATH=src python3 -m webhook_forge.cli ...
```

## Quickstart

### 1. Clone the repository
```bash
git clone https://github.com/wzh886/webhook-forge.git
cd webhook-forge
```

### 2. Run locally
```bash
PYTHONPATH=src python3 -m webhook_forge.cli sign \
  --secret whsec_test \
  --timestamp 1712345678 \
  --payload '{"ok":true}'
```

Verify a signature:

```bash
PYTHONPATH=src python3 -m webhook_forge.cli verify \
  --secret whsec_test \
  --timestamp 1712345678 \
  --payload '{"ok":true}' \
  --signature 'sha256=your_signature_here'
```

### 3. Install as a local CLI (optional)
```bash
pip install -e .
webhook-forge sign --secret whsec_test --timestamp 1712345678 --payload '{"ok":true}'
```

## Sample output

### Sign
```bash
$ webhook-forge sign --secret whsec_test --timestamp 1712345678 --payload '{"ok":true}'
sha256=6d4f...
```

### Verify
```bash
$ webhook-forge verify --secret whsec_test --timestamp 1712345678 --payload '{"ok":true}' --signature 'sha256=6d4f...'
valid
```

---

## Roadmap
### v0.1
- [x] core sign/verify helpers
- [x] CLI scaffold
- [x] minimal tests

### v0.2
- [ ] replay saved webhook events to arbitrary endpoints
- [ ] pretty-print request/response inspection output
- [ ] support loading payloads from files/stdin
- [ ] timestamp tolerance verification

### v0.3
- [ ] local delivery history store
- [ ] response timing metrics
- [ ] structured export of replay sessions
- [ ] provider-specific presets (Stripe-style, generic HMAC, custom headers)

### v0.4
- [ ] lightweight TUI or web debug panel
- [ ] queue/retry simulation helpers
- [ ] integration test fixtures for backend projects

---

## Example use cases
- validating a new webhook integration before shipping
- reproducing failed deliveries from production logs
- testing signature verification code in local development
- building more reliable webhook-driven systems
- teaching or documenting webhook delivery semantics

---

## Design principles
- **simple first**: standard-library-first where possible
- **debuggable**: optimize for visibility and reproducibility
- **scriptable**: useful in shell pipelines and automation
- **extensible**: small core, room for replay and inspection modules

---

## Project status
This repository is intentionally small today. The goal is not to look large; the goal is to become a sharp, reliable utility that is genuinely useful in real integration work.

If you work on APIs, automation, or outbound event systems, this project is meant to become part of that toolbox.

---

## Tech
- Python 3.11+
- standard library first
- test-friendly module layout
