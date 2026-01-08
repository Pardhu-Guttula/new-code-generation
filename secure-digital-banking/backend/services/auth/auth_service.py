from typing import Optional
from jose import JWTError, jwt
from passlib.context import CryptContext
from backend.models.auth.user import User
from backend.repositories.users.user_repository import UserRepository

class AuthService:
    def __init__(self, user_repository: UserRepository, secret_key: str, algorithm: str):
        self.user_repository = user_repository
        self.secret_key = secret_key
        self.algorithm = algorithm
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return self.pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password: str) -> str:
        return self.pwd_context.hash(password)

    def create_access_token(self, data: dict, expires_delta: Optional[int] = None) -> str:
        to_encode = data.copy()
        if expires_delta:
            to_encode['exp'] = expires_delta
        return jwt.encode(to_encode, self.secret_key, algorithm=self.algorithm)

    def authenticate_user(self, username: str, password: str) -> Optional[User]:
        user = self.user_repository.find_by_username(username)
        if not user or not self.verify_password(password, user.hashed_password):
            return None
        return user