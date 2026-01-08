from flask import Blueprint, request, jsonify
from backend.services.auth.auth_service import AuthService
from backend.repositories.users.user_repository import UserRepository
from backend.repositories.sessions.session_repository import SessionRepository

user_blueprint = Blueprint('user', __name__)
user_repository = UserRepository()
session_repository = SessionRepository()
auth_service = AuthService(user_repository, session_repository)

@user_blueprint.route('/register', methods=['POST'])
def register():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    user = auth_service.register_user(email, password)
    return jsonify(user.dict()), 201

@user_blueprint.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    session = auth_service.authenticate_user(email, password)
    if session:
        auth_service.reset_login_attempts(email)
        return jsonify(session.dict()), 200
    else:
        auth_service.increase_login_attempts(email)
        return jsonify({"error": "Invalid credentials"}), 401