from typing import Optional
from backend.models.auth.user import User

class UserRepository:
    def create(self, user: User) -> User:
        # Dummy implementation; replace with actual database save logic
        pass

    def find_by_id(self, user_id: int) -> Optional<User]:
        # Dummy implementation; replace with actual database query
        pass

    def find_by_username(self, username: str) -> Optional<User]:
        # Dummy implementation; replace with actual database query
        pass

    def update(self, user: User) -> User:
        # Dummy implementation; replace with actual database update logic
        pass

    def delete(self, user_id: int) -> None:
        # Dummy implementation; replace with actual database delete logic
        pass