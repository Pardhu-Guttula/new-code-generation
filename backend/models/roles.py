from datetime import datetime
from pydantic import BaseModel, Field

class Role(BaseModel):
    id: int = Field(..., primary_key=True, autoincrement=True)
    name: str
    description: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    
    class Config:
        orm_mode = True