from datetime import datetime
from pydantic import BaseModel, Field

class Account(BaseModel):
    id: int = Field(..., primary_key=True, autoincrement=True)
    user_id: int
    account_number: str
    account_type: str
    balance: float
    created_at: datetime = Field(default_factory=datetime.utcnow)
    
    class Config:
        orm_mode = True