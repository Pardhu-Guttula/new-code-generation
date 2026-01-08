from backend.models.users.user import User
from typing import List, Optional

class UserRepository:
    def get_user_by_id(self, user_id: int) -> Optional[User]:
        pass  # Implement database retrieval logic here

    def get_user_by_email(self, email: str) -> Optional[User]:
        pass  # Implement database retrieval logic here

    def create_user(self, user: User) -> User:
        pass  # Implement database creation logic here

    def update_user(self, user: User) -> User:
        pass  # Implement database update logic here

    def delete_user(self, user_id: int) -> None:
        pass  # Implement database deletion logic here

    def list_users(self) -> List[User]:
        pass  # Implement database list retrieval logic here