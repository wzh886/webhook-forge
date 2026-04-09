from __future__ import annotations

import hashlib
import hmac


def sign_payload(secret: str, timestamp: str, payload: str) -> str:
    signed = f"{timestamp}.{payload}".encode("utf-8")
    digest = hmac.new(secret.encode("utf-8"), signed, hashlib.sha256).hexdigest()
    return f"sha256={digest}"


def verify_signature(secret: str, timestamp: str, payload: str, received: str) -> bool:
    expected = sign_payload(secret, timestamp, payload)
    return hmac.compare_digest(expected, received)
