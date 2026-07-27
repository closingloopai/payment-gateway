"""Refund a charge, fully or partially."""
from payments.errors import RefundTooLargeError

def refund(charge, amount_cents):
    """Refund ``amount_cents`` against ``charge``.

    BUG: it does not cap the refund at the remaining refundable amount
    (amount_cents - refunded_cents), so you can refund MORE than was captured and
    drive refunded_cents above the charge total. Reject an over-refund with
    RefundTooLargeError and update status to refunded / partially_refunded.
    """
    charge.refunded_cents += amount_cents
    if charge.refunded_cents >= charge.amount_cents:
        charge.status = "refunded"
    else:
        charge.status = "partially_refunded"
    return charge
