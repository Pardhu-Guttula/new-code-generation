from datetime import datetime
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class User:
    id: int
    email: str
    password: str
    first_name: str
    last_name: str
    phone_number: str
    login_attempts: int
    is_locked: bool
    last_login_at: datetime
    created_at: datetime
    updated_at: datetime