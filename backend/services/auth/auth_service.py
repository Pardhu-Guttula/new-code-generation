from backend.repositories.users.user_repository import UserRepository
from backend.models.users.user import User
from pydantic import EmailStr

class AuthService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def register_user(self, email: EmailStr, password: str) -> User:
        # Hash the password before storing
        hashed_password = self._hash_password(password)
        user = User(email=email, password=hashed_password)
        return self.user_repository.create_user(user)

    def _hash_password(self, password: str) -> str:
        # Implement password hashing logic here
        pass

    def authenticate_user(self, email: EmailStr, password: str) -> bool:
        # Implement authentication logic
        pass