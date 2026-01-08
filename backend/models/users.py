from datetime import datetime
from pydantic import BaseModel, EmailStr, Field

class User(BaseModel):
    id: int = Field(..., primary_key=True, autoincrement=True)
    email: EmailStr
    password: str
    first_name: str
    last_name: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    
    class Config:
        orm_mode = True