import logging
import re
from backend.repositories.users.user_repository import UserRepository
from backend.models.users.user import User

logger = logging.getLogger(__name__)

class RegistrationService:
    def __init__(self, user_repo: UserRepository) -> None:
        self._user_repo = user_repo

    def register_user(self, email: str, password: str) -> User:
        if not self._is_valid_email(email):
            raise ValueError("Invalid email format")
        if not self._is_strong_password(password):
            raise ValueError("Password does not meet security criteria")
        existing_user = self._user_repo.get_user_by_email(email)
        if existing_user:
            raise ValueError("Email is already in use")
        logger.info("Registering new user with email=%s", email)
        return self._user_repo.create_user(email, password)

    @staticmethod
    def _is_valid_email(email: str) -> bool:
        return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))

    @staticmethod
    def _is_strong_password(password: str) -> bool:
        return len(password) >= 8 and any(char.isdigit() for char in password) and any(char.isalpha() for char in password)