from flask import Blueprint, request, jsonify
from backend.repositories.users.user_repository import UserRepository
from backend.services.auth.auth_service import AuthService

auth_controller = Blueprint('auth_controller', __name__)
user_repository = UserRepository()
auth_service = AuthService(user_repository, secret_key="your-secret-key")

@auth_controller.route('/auth/register', methods=['POST'])
def register_user():
    json_data = request.json
    email = json_data.get('email')
    password = json_data.get('password')
    full_name = json_data.get('full_name')

    if user_repository.find_by_email(email):
        return jsonify({'message': 'User already exists'}), 400

    hashed_password = auth_service.get_password_hash(password)
    user = User(email=email, password=hashed_password, full_name=full_name)
    user_repository.create(user)
    return jsonify({'message': 'User registered successfully'}), 201

@auth_controller.route('/auth/login', methods=['POST'])
def login_user():
    json_data = request.json
    email = json_data.get('email')
    password = json_data.get('password')

    user = auth_service.authenticate_user(email, password)
    if not user:
        return jsonify({'message': 'Invalid credentials'}), 401

    access_token = auth_service.create_access_token(user.id)
    return jsonify({'access_token': access_token}), 200