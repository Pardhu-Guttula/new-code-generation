from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr

class PasswordReset(BaseModel):
    id: int
    user_id: int
    reset_token: str
    email: EmailStr
    is_used: bool
    expires_at: datetime
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True