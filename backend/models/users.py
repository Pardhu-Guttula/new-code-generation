from datetime import datetime
from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class User(BaseModel):
    id: int = Field(..., primary_key=True, autoincrement=True)
    email: EmailStr
    password: str
    mfa_enabled: bool = Field(..., default=False)
    mfa_secret: Optional[str] = Field(None)
    is_active: bool = Field(..., default=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    
    class Config:
        orm_mode = True