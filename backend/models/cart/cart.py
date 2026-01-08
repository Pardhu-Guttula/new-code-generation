from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class CartItem(BaseModel):
    product_id: int
    quantity: int

class Cart(BaseModel):
    user_id: Optional[int]
    items: List[CartItem]
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True