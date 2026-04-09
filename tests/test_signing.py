from webhook_forge.signing import sign_payload, verify_signature


def test_sign_and_verify_round_trip():
    secret = "whsec_test"
    timestamp = "1712345678"
    payload = '{"ok":true}'
    signature = sign_payload(secret, timestamp, payload)
    assert verify_signature(secret, timestamp, payload, signature) is True


def test_verify_rejects_wrong_signature():
    assert verify_signature("a", "1", "{}", "sha256=deadbeef") is False
