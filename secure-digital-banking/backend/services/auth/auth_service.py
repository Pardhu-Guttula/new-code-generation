from typing import Optional
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
from backend.models.users.user import User
from backend.repositories.users.user_repository import UserRepository
from backend.models.auth.masked_password_policy import MaskedPasswordPolicy

class AuthService:
    def __init__(self, 
                 user_repository: UserRepository, 
                 secret_key: str, 
                 algorithm: str = 'HS256', 
                 token_expire_minutes: int = 30,
                 masked_password_policy: Optional[MaskedPasswordPolicy] = None):
        self.user_repository = user_repository
        self.secret_key = secret_key
        self.algorithm = algorithm
        self.token_expire_minutes = token_expire_minutes
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        self.masked_password_policy = masked_password_policy

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return self.pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password: str) -> str:
        return self.pwd_context.hash(password)

    def authenticate_user(self, email: str, password: str) -> Optional[User]:
        user = self.user_repository.find_by_email(email)
        if user and self.verify_password(password, user.password):
            return user
        return None

    def create_access_token(self, user_id: int) -> str:
        to_encode = {"sub": str(user_id), "exp": datetime.utcnow() + timedelta(minutes=self.token_expire_minutes)}
        return jwt.encode(to_encode, self.secret_key, algorithm=self.algorithm)

    def mask_password(self, password: str) -> str:
        if not self.masked_password_policy:
            return password
        return self.masked_password_policy.mask_password(password)