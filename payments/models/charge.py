from dataclasses import dataclass, field
@dataclass
class Charge:
    id: str
    amount_cents: int
    currency: str = "usd"
    status: str = "succeeded"        # succeeded | refunded | partially_refunded
    refunded_cents: int = 0
    idempotency_key: str | None = None
