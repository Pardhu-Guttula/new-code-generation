from flask import Blueprint, jsonify
from backend.repositories.accounts.account_repository import AccountRepository
from backend.repositories.requests.request_repository import RequestRepository
from backend.services.dashboard.dashboard_service import DashboardService

dashboard_controller = Blueprint('dashboard_controller', __name__)

account_repository = AccountRepository()
request_repository = RequestRepository()
dashboard_service = DashboardService(account_repository, request_repository)

@dashboard_controller.route('/dashboard/overview/<int:user_id>', methods=['GET'])
def get_dashboard_overview(user_id: int):
    overview = dashboard_service.get_dashboard_overview(user_id)
    return jsonify(overview.dict()), 200