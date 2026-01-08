from datetime import datetime
from typing import Optional
from pydantic import BaseModel, constr, condecimal

class Product(BaseModel):
    id: int
    name: constr(min_length=1)
    description: constr(min_length=1)
    price: condecimal(gt=0)
    category: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True