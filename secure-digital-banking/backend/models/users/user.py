from datetime import datetime
from pydantic import BaseModel, Field

class User(BaseModel):
    id: int = Field(..., primary_key=True, autoincrement=True)
    email: str
    password: str
    full_name: str
    is_active: bool = Field(default=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        orm_mode = True