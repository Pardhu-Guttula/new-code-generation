from typing import Optional, List
from backend.models.accounts import Account
from backend.models.account_request import AccountRequest
from backend.repositories.accounts import AccountRepository
from backend.repositories.account_request_repository import AccountRequestRepository

class AccountService:
    def __init__(self, account_repository: AccountRepository, account_request_repository: AccountRequestRepository):
        self.account_repository = account_repository
        self.account_request_repository = account_request_repository

    def open_account(self, user_id: int, account_type: str) -> AccountRequest:
        account_request = AccountRequest(user_id=user_id, account_type=account_type)
        return self.account_request_repository.create(account_request)

    def get_user_account_requests(self, user_id: int) -> List[AccountRequest]:
        return self.account_request_repository.find_by_user_id(user_id)

    def create_account_from_request(self, account_request: AccountRequest) -> Account:
        account = Account(
            user_id=account_request.user_id,
            account_number="ACC" + str(account_request.user_id).zfill(8),
            account_type=account_request.account_type,
            balance=0.0
        )
        self.account_request_repository.update(account_request)
        return self.account_repository.create(account)