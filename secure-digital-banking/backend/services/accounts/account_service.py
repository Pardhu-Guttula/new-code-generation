from typing import List
from backend.models.accounts.account import Account
from backend.repositories.accounts.account_repository import AccountRepository

class AccountService:
    def __init__(self, account_repository: AccountRepository):
        self.account_repository = account_repository

    def create_account(self, user_id: int, account_number: str, balance: float) -> Account:
        account = Account(user_id=user_id, account_number=account_number, balance=balance)
        return self.account_repository.create(account)

    def get_account(self, account_id: int) -> Account:
        return self.account_repository.find_by_id(account_id)

    def get_user_accounts(self, user_id: int) -> List<Account]:
        return self.account_repository.find_by_user_id(user_id)

    def update_account(self, account: Account) -> Account:
        return self.account_repository.update(account)

    def delete_account(self, account_id: int) -> None:
        self.account_repository.delete(account_id)