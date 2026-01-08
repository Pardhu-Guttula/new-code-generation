from typing import List
from backend.models.user_roles import UserRole

class UserRoleRepository:
    def create(self, user_role: UserRole) -> UserRole:
        # Dummy implementation; replace with actual database save logic
        pass

    def find_by_user_id(self, user_id: int) -> List<UserRole]:
        # Dummy implementation; replace with actual database query
        pass

    def delete_by_user_id(self, user_id: int) -> None:
        # Dummy implementation; replace with actual database delete logic
        pass