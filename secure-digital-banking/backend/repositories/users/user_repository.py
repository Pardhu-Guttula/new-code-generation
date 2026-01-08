from typing import Optional, List
from backend.models.users.user import User

class UserRepository:
    def create(self, user: User) -> User:
        # Dummy implementation; replace with actual database save logic
        pass

    def find_by_id(self, user_id: int) -> Optional<User]:
        # Dummy implementation; replace with actual database query
        pass

    def find_by_email(self, email: str) -> Optional<User]:
        # Dummy implementation; replace with actual database query
        pass

    def update(self, user: User) -> User:
        # Dummy implementation; replace with actual database update logic
        pass

    def delete(self, user_id: int) -> None:
        # Dummy implementation; replace with actual database delete logic
        pass