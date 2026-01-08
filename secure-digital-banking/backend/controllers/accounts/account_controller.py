from flask import Blueprint, request, jsonify
from backend.repositories.accounts.account_repository import AccountRepository
from backend.services.accounts.account_service import AccountService

account_controller = Blueprint('account_controller', __name__)
account_repository = AccountRepository()
account_service = AccountService(account_repository)

@account_controller.route('/accounts', methods=['POST'])
def create_account():
    json_data = request.json
    user_id = json_data.get('user_id')
    account_number = json_data.get('account_number')
    balance = json_data.get('balance')

    account = account_service.create_account(user_id, account_number, balance)
    return jsonify(account.dict()), 201

@account_controller.route('/accounts/<int:account_id>', methods=['GET'])
def get_account(account_id: int):
    account = account_service.get_account(account_id)
    return jsonify(account.dict()), 200

@account_controller.route('/accounts/user/<int:user_id>', methods=['GET'])
def get_user_accounts(user_id: int):
    accounts = account_service.get_user_accounts(user_id)
    return jsonify([account.dict() for account in accounts]), 200

@account_controller.route('/accounts/<int:account_id>', methods=['PUT'])
def update_account(account_id: int):
    json_data = request.json
    account = account_service.get_account(account_id)
    
    if not account:
        return jsonify({'message': 'Account not found'}), 404
    
    account_data = json_data.dict()
    updated_account = account_service.update_account(account_data)
    return jsonify(updated_account.dict()), 200

@account_controller.route('/accounts/<int:account_id>', methods=['DELETE'])
def delete_account(account_id: int):
    account_service.delete_account(account_id)
    return jsonify({'message': 'Account deleted successfully'}), 200