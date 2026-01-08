from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class CartItem:
    product_id: int
    quantity: int