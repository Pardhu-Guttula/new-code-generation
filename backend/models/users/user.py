from datetime import datetime
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    id: int
    email: EmailStr
    password: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True