"""In-memory idempotency store keyed by client-supplied key."""
class IdempotencyStore:
    def __init__(self):
        self._seen = {}
    def get(self, key):
        return self._seen.get(key)
    def put(self, key, charge_id):
        self._seen[key] = charge_id
