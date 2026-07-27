"""Create charges. Retries must be idempotent."""
import uuid
from payments.models.charge import Charge

def create_charge(amount_cents, idempotency_key, store, ledger):
    """Create a charge, or return the existing one for a repeated idempotency key.

    BUG: it never consults ``store`` before creating the charge, so a client that
    retries the same request (same idempotency_key) gets a SECOND real charge --
    a double charge. It must return the already-created charge when the key was
    seen, and only create + record a new one when it wasnt.
    """
    cid = f"ch_{uuid.uuid4().hex[:12]}"
    charge = Charge(id=cid, amount_cents=amount_cents, idempotency_key=idempotency_key)
    ledger[cid] = charge
    store.put(idempotency_key, cid)
    return charge
