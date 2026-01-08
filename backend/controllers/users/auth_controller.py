from flask import Blueprint, request, jsonify
from backend.services.auth.auth_service.py import AuthService
from backend.repositories.users.user_repository import UserRepository

auth_controller = Blueprint('auth_controller', __name__)
user_repository = UserRepository()
auth_service = AuthService(user_repository)

@auth_controller.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    mfa_token = data.get('mfa_token')
    user = auth_service.authenticate(email, password, mfa_token)
    if user:
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'Invalid credentials or MFA token'}), 401

@auth_controller.route('/enable-mfa', methods=['POST'])
def enable_mfa():
    data = request.json
    email = data.get('email')
    user = user_repository.find_by_email(email)
    if user:
        secret = auth_service.enable_mfa(user)
        return jsonify({'message': 'MFA enabled', 'secret': secret}), 200
    else:
        return jsonify({'message': 'User not found'}), 404