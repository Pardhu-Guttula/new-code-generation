from flask import Blueprint, jsonify, request
from backend.services.user_management.user_service.py import UserService
from backend.repositories.users.user_repository import UserRepository
from backend.repositories.accounts.account_repository import AccountRepository

dashboard_controller = Blueprint('dashboard_controller', __name__)
user_repository = UserRepository()
account_repository = AccountRepository()
user_service = UserService(user_repository, account_repository)

@dashboard_controller.route('/dashboard', methods=['GET'])
def dashboard():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({'message': 'User ID is required'}), 400

    data = user_service.get_user_dashboard(int(user_id))
    if not data:
        return jsonify({'message': 'User not found'}), 404

    return jsonify(data), 200