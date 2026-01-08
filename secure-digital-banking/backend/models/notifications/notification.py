from datetime import datetime
from pydantic import BaseModel, Field

class Notification(BaseModel):
    id: int = Field(..., primary_key=True, autoincrement=True)
    user_id: int
    type: str
    message: str
    sent_at: datetime = Field(default_factory=datetime.utcnow)
    read: bool = Field(default=False)

    class Config:
        orm_mode = True