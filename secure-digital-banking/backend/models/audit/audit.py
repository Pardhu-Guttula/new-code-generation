from datetime import datetime
from pydantic import BaseModel, Field

class Audit(BaseModel):
    id: int = Field(..., primary_key=True, autoincrement=True)
    user_id: int
    action: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    details: str = Field(default='')

    class Config:
        orm_mode = True