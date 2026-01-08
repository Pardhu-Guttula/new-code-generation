from flask import Blueprint, request, jsonify
from backend.services.account_management.account_service import AccountService
from backend.repositories.accounts import AccountRepository
from backend.repositories.account_request_repository import AccountRequestRepository

account_controller = Blueprint('account_controller', __name__)
account_repository = AccountRepository()
account_request_repository = AccountRequestRepository()
account_service = AccountService(account_repository, account_request_repository)

@account_controller.route('/open-account', methods=['POST'])
def open_account():
    data = request.json
    user_id = data.get('user_id')
    account_type = data.get('account_type')
    
    if not user_id or not account_type:
        return jsonify({'message': 'User ID and Account Type are required'}), 400
    
    account_request = account_service.open_account(user_id, account_type)
    return jsonify(account_request.dict()), 201

@account_controller.route('/account-requests', methods=['GET'])
def account_requests():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({'message': 'User ID is required'}), 400
    
    requests = account_service.get_user_account_requests(int(user_id))
    return jsonify([request.dict() for request in requests]), 200