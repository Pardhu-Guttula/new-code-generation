import logging
from backend.repositories.users.user_repository import UserRepository
import bcrypt

logger = logging.getLogger(__name__)

class LoginService:
    def __init__(self, user_repo: UserRepository) -> None:
        self._user_repo = user_repo

    def login(self, email: str, password: str) -> bool:
        user = self._user_repo.get_user_by_email(email)
        if not user:
            raise ValueError("User not found")
        if user.is_locked:
            raise PermissionError("Account is locked due to too many failed login attempts")
        if bcrypt.checkpw(password.encode(), user.password.encode()):
            logger.info("Successful login for user_id=%s", user.id)
            self._user_repo.update_last_login(user.id)
            return True
        else:
            logger.warning("Failed login attempt for user_id=%s", user.id)
            self._user_repo.update_user_login_attempts(user.id, user.login_attempts + 1)
            return False