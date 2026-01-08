from datetime import datetime
from pydantic import BaseModel, Field

class AuditLog(BaseModel):
    id: int = Field(..., primary_key=True, autoincrement=True)
    user_id: int
    action: str
    details: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        orm_mode = True