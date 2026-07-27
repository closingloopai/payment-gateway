"""Create charges. Retries must be idempotent."""
import uuid
from payments.models.charge import Charge


def create_charge(amount_cents, idempotency_key, store, ledger):
    """Create a charge, or return the existing one for a repeated idempotency key.

    A retried request with the same idempotency key must NOT create a second
    charge: we look it up first and return the already-created charge when the
    key was seen, only creating (and recording) a new one when it wasn't.
    """
    existing_cid = store.get(idempotency_key)
    if existing_cid is not None and existing_cid in ledger:
        return ledger[existing_cid]
    cid = f"ch_{uuid.uuid4().hex[:12]}"
    charge = Charge(id=cid, amount_cents=amount_cents, idempotency_key=idempotency_key)
    ledger[cid] = charge
    store.put(idempotency_key, cid)
    return charge
