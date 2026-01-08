from typing import Optional
from backend.models.users import User

class UserRepository:
    def find_by_id(self, user_id: int) -> Optional[User]:
        # Dummy implementation; replace with actual database query
        pass