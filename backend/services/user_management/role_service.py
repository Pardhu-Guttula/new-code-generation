from typing import List
from backend.models.roles import Role
from backend.models.user_roles import UserRole
from backend.repositories.roles.role_repository import RoleRepository
from backend.repositories.user_roles.user_role_repository import UserRoleRepository

class RoleService:
    def __init__(self, role_repository: RoleRepository, user_role_repository: UserRoleRepository):
        self.role_repository = role_repository
        self.user_role_repository = user_role_repository

    def create_role(self, name: str, description: str) -> Role:
        role = Role(name=name, description=description)
        return self.role_repository.create(role)

    def get_role(self, role_id: int) -> Role:
        return self.role_repository.find_by_id(role_id)

    def get_all_roles(self) -> List<Role]:
        return self.role_repository.find_all()

    def update_role(self, role: Role) -> Role:
        return self.role_repository.update(role)

    def delete_role(self, role_id: int) -> None:
        self.role_repository.delete(role_id)

    def assign_role_to_user(self, user_id: int, role_id: int) -> UserRole:
        user_role = UserRole(user_id=user_id, role_id=role_id)
        return self.user_role_repository.create(user_role)
    
    def get_user_roles(self, user_id: int) -> List[UserRole]:
        return self.user_role_repository.find_by_user_id(user_id)

    def revoke_roles_from_user(self, user_id: int) -> None:
        self.user_role_repository.delete_by_user_id(user_id)