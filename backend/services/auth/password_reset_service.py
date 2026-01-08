import logging
import secrets
import hashlib
from datetime import datetime, timedelta
from backend.repositories.users.user_repository import UserRepository
from backend.models.users.user import User
from backend.models.users.password_reset import PasswordReset

logger = logging.getLogger(__name__)

class PasswordResetService:
    def __init__(self, user_repo: UserRepository) -> None:
        self._user_repo = user_repo

    def initiate_reset(self, email: str) -> PasswordReset:
        user = self._user_repo.get_user_by_email(email)
        if not user:
            raise ValueError("User with given email not found")
        token = secrets.token_urlsafe()
        expires_at = datetime.now() + timedelta(hours=24)
        return self._user_repo.create_password_reset_token(user.id, token, expires_at)

    def validate_token(self, token: str) -> User:
        reset = self._user_repo.get_password_reset_by_token(token)
        if not reset:
            raise ValueError("Invalid or expired password reset token")
        if reset.expires_at < datetime.now():
            raise ValueError("Password reset token has expired")
        return self._user_repo.get_user_by_email(reset.user_id)

    def reset_password(self, token: str, new_password: str) -> None:
        reset = self._user_repo.get_password_reset_by_token(token)
        if not reset:
            raise ValueError("Invalid or expired password reset token")
        if reset.expires_at < datetime.now():
            raise ValueError("Password reset token has expired")
        hashed_password = hashlib.sha256(new_password.encode()).hexdigest()
        self._user_repo.update_user_password(reset.user_id, hashed_password)