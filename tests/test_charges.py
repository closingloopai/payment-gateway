from payments.services.charges import create_charge
from payments.services.idempotency import IdempotencyStore

def test_retry_is_idempotent():
    store, ledger = IdempotencyStore(), {}
    a = create_charge(500, "key-1", store, ledger)
    b = create_charge(500, "key-1", store, ledger)  # retry
    assert a.id == b.id, "same idempotency key must not double charge"
    assert len(ledger) == 1
