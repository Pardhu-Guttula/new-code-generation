from backend.models.dashboard.overview import DashboardOverview
from backend.repositories.accounts.account_repository import AccountRepository
from backend.repositories.requests.request_repository import RequestRepository

class DashboardService:
    def __init__(self, account_repository: AccountRepository, request_repository: RequestRepository):
        self.account_repository = account_repository
        self.request_repository = request_repository

    def get_dashboard_overview(self, user_id: int) -> DashboardOverview:
        accounts = self.account_repository.find_by_user_id(user_id)
        total_balance = sum(account.balance for account in accounts)
        
        requests = self.request_repository.find_by_user_id(user_id)
        upcoming_bills = len([request for request in requests if request.type == 'bill' and request.status == 'upcoming'])
        recent_transactions = len([request for request in requests if request.type == 'transaction'])

        overview = DashboardOverview(
            user_id=user_id,
            total_balance=total_balance,
            upcoming_bills=upcoming_bills,
            recent_transactions=recent_transactions
        )
        return overview