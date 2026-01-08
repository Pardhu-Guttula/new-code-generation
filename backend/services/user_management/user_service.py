from typing import Dict, Any
from backend.repositories.users import UserRepository
from backend.repositories.accounts import AccountRepository

class UserService:
    def __init__(self, user_repository: UserRepository, account_repository: AccountRepository):
        self.user_repository = user_repository
        self.account_repository = account_repository

    def get_user_dashboard(self, user_id: int) -> Dict[str, Any]:
        user = self.user_repository.find_by_id(user_id)
        if not user:
            return {}
        
        accounts = self.account_repository.find_by_user_id(user_id)
        return {
            "user": user,
            "accounts": accounts
        }