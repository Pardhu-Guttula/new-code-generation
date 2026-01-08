from datetime import datetime
from pydantic import BaseModel, Field

class Request(BaseModel):
    id: int = Field(..., primary_key=True, autoincrement=True)
    user_id: int
    type: str
    details: str
    status: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        orm_mode = True