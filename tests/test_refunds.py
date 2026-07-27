import pytest
from payments.models.charge import Charge
from payments.services.refunds import refund
from payments.errors import RefundTooLargeError

def test_cannot_over_refund():
    ch = Charge(id="ch_1", amount_cents=1000)
    refund(ch, 600)
    with pytest.raises(RefundTooLargeError):
        refund(ch, 600)  # only 400 left
