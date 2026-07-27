"""Verify inbound provider webhooks."""
import hashlib, hmac
from payments.errors import InvalidSignatureError

def verify(payload: bytes, signature: str, secret: str) -> bool:
    """Verify the HMAC-SHA256 signature of a webhook payload.

    BUG: it compares the signatures with ``==``, which is not constant-time and
    leaks timing. Use hmac.compare_digest. (It also should reject an empty
    signature outright.)
    """
    expected = hmac.new(secret.encode(), payload, hashlib.sha256).hexdigest()
    if expected == signature:
        return True
    raise InvalidSignatureError("bad signature")
