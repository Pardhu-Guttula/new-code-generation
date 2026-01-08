from datetime import datetime
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class User:
    id: int
    email: str
    password: str
    created_at: datetime
    updated_at: datetime