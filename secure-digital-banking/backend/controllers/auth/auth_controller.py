from datetime import timedelta
from flask import Blueprint, request, jsonify
from backend.services.auth.auth_service import AuthService
from backend.repositories.users.user_repository import UserRepository

auth_controller = Blueprint('auth_controller', __name__)

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

user_repository = UserRepository()
auth_service = AuthService(user_repository, SECRET_KEY, ALGORITHM)

@auth_controller.route('/login', methods=['POST'])
def login():
    json_data = request.json
    username = json_data.get('username')
    password = json_data.get('password')
    
    user = auth_service.authenticate_user(username, password)
    if not user:
        return jsonify({'message': 'Invalid credentials'}), 401

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth_service.create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)
    return jsonify(access_token=access_token), 200

@auth_controller.route('/register', methods=['POST'])
def register():
    json_data = request.json
    username = json_data.get('username')
    password = json_data.get('password')
    email = json_data.get('email')
    
    hashed_password = auth_service.get_password_hash(password)
    user = User(username=username, email=email, hashed_password=hashed_password)
    created_user = user_repository.create(user)
    
    return jsonify(created_user.dict()), 201