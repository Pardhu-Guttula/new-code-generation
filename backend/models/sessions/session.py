from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class Session(BaseModel):
    id: int
    user_id: int
    session_token: str
    is_active: bool
    expires_at: datetime
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True