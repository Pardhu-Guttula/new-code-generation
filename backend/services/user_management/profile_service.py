import logging
from backend.repositories.users.user_repository import UserRepository
from backend.models.users.user import User

logger = logging.getLogger(__name__)

class ProfileService:
    def __init__(self, user_repo: UserRepository) -> None:
        self._user_repo = user_repo

    def update_profile(self, user_id: int, first_name: str, last_name: str, phone_number: str) -> User:
        user = self._user_repo.get_user_by_id(user_id)
        if not user:
            raise ValueError("User not found")
        logger.info("Updating profile information for user_id=%s", user_id)
        self._user_repo.update_user_profile(user_id, first_name, last_name, phone_number)
        return self._user_repo.get_user_by_id(user_id)