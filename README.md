# webhook-forge

A compact developer tool for inspecting, signing, verifying, replaying, and debugging outbound webhook deliveries.

## Why it exists
Modern integrations fail in boring but expensive ways: bad signatures, missing retries, mismatched payloads, and poor observability. `webhook-forge` is designed to make webhook debugging and local validation faster.

## Planned capabilities
- sign webhook payloads with HMAC-SHA256
- verify inbound signatures locally
- replay stored deliveries to target endpoints
- inspect headers, latency, and response outcomes
- provide a simple CLI for delivery debugging workflows

## Example use cases
- validating a new webhook integration before shipping
- reproducing failed deliveries from production logs
- testing signature verification code in local dev
- building reliable webhook-driven systems

## Status
Initial scaffold. The first version focuses on a clean CLI surface and reusable signature helpers.

## Tech
- Python 3.11+
- standard library first
- test-friendly module layout
