from datetime import datetime
from pydantic import BaseModel, EmailStr, Field

class AccountRequest(BaseModel):
    id: int = Field(..., primary_key=True, autoincrement=True)
    user_id: int
    account_type: str
    status: str = Field(default="pending")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    
    class Config:
        orm_mode = True