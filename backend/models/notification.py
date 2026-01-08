from datetime import datetime
from pydantic import BaseModel, Field

class Notification(BaseModel):
    id: int = Field(..., primary_key=True, autoincrement=True)
    user_id: int
    message: str
    status: str = Field(default="pending")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    
    class Config:
        orm_mode = True