from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr

class Profile(BaseModel):
    id: int
    user_id: int
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: EmailStr
    phone: Optional[str] = None
    address: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True