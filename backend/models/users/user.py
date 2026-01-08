from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, constr

class User(BaseModel):
    id: int
    email: EmailStr
    password: constr(min_length=8)
    login_attempts: int = 0
    is_locked: bool = False
    last_login_at: Optional[datetime] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True