from dataclasses import dataclass
from datetime import datetime
from typing import List
from backend.models.cart.cart_item import CartItem

@dataclass(frozen=True, slots=True)
class ShoppingCart:
    user_id: int
    items: List[CartItem]
    created_at: datetime
    updated_at: datetime