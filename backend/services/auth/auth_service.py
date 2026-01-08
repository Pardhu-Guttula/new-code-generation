import bcrypt
import pyotp
from datetime import datetime
from typing import Optional
from backend.models.users import User
from backend.repositories.users import UserRepository

class AuthService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def hash_password(self, password: str) -> str:
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def check_password(self, user: User, password: str) -> bool:
        return bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8'))

    def enable_mfa(self, user: User) -> str:
        user.mfa_secret = pyotp.random_base32()
        user.mfa_enabled = True
        self.user_repository.update_user(user)
        return user.mfa_secret

    def verify_mfa_token(self, user: User, token: str) -> bool:
        if not user.mfa_enabled or not user.mfa_secret:
            return False
        totp = pyotp.TOTP(user.mfa_secret)
        return totp.verify(token)

    def authenticate(self, email: str, password: str, mfa_token: Optional[str] = None) -> Optional[User]:
        user = self.user_repository.find_by_email(email)
        if user and self.check_password(user, password):
            if user.mfa_enabled:
                if mfa_token is None or not self.verify_mfa_token(user, mfa_token):
                    return None
            user.last_login_at = datetime.utcnow()
            self.user_repository.update_user(user)
            return user
        return None