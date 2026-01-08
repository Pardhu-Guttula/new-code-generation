from datetime import datetime
from typing import Optional
from pydantic import BaseModel, constr

class Category(BaseModel):
    id: int
    name: constr(min_length=1)
    parent_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True