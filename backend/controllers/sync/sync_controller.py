from flask import Blueprint, request, jsonify
from backend.integrations.core_banking.client import CoreBankingClient
from backend.services.core_banking_sync import CoreBankingSyncService

sync_controller = Blueprint('sync_controller', __name__)

core_banking_client = CoreBankingClient(base_url='https://core-banking-api.example.com', api_key='your_api_key')
core_banking_sync_service = CoreBankingSyncService(core_banking_client)

@sync_controller.route('/sync/user', methods=['POST'])
def sync_user():
    user_data = request.json
    if not user_data:
        return jsonify({'message': 'User data is required'}), 400

    try:
        result = core_banking_sync_service.sync_user_data(user_data)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@sync_controller.route('/sync/account', methods=['POST'])
def sync_account():
    account_data = request.json
    if not account_data:
        return jsonify({'message': 'Account data is required'}), 400

    try:
        result = core_banking_sync_service.sync_account_data(account_data)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500