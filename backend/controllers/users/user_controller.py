from flask import Blueprint, request, jsonify
from backend.services.auth.auth_service import AuthService
from backend.services.profile.profile_service import ProfileService
from backend.repositories.users.user_repository import UserRepository
from backend.repositories.sessions.session_repository import SessionRepository
from backend.repositories.password_reset.password_reset_repository import PasswordResetRepository
from backend.repositories.profile.profile_repository import ProfileRepository

user_blueprint = Blueprint('user', __name__)
user_repository = UserRepository()
session_repository = SessionRepository()
password_reset_repository = PasswordResetRepository()
profile_repository = ProfileRepository()
auth_service = AuthService(user_repository, session_repository, password_reset_repository)
profile_service = ProfileService(profile_repository)

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

@user_blueprint.route('/request_password_reset', methods=['POST'])
def request_password_reset():
    data = request.json
    email = data.get('email')
    password_reset = auth_service.request_password_reset(email)
    return jsonify(password_reset.dict()), 201

@user_blueprint.route('/reset_password', methods=['POST'])
def reset_password():
    data = request.json
    token = data.get('token')
    new_password = data.get('new_password')
    user = auth_service.reset_password(token, new_password)
    return jsonify(user.dict()), 200

@user_blueprint.route('/profile', methods=['POST'])
def create_profile():
    data = request.json
    profile = profile_service.create_profile(data)
    return jsonify(profile.dict()), 201

@user_blueprint.route('/profile/<int:profile_id>', methods=['PUT'])
def update_profile(profile_id):
    data = request.json
    profile = profile_service.update_profile(profile_id, data)
    return jsonify(profile.dict()), 200

@user_blueprint.route('/profile/<int:profile_id>', methods=['GET'])
def get_profile(profile_id):
    profile = profile_service.get_profile(profile_id)
    return jsonify(profile.dict()), 200

@user_blueprint.route('/profile/<int:profile_id>', methods=['DELETE'])
def delete_profile(profile_id):
    profile_service.delete_profile(profile_id)
    return jsonify({"message": "Profile deleted"}), 200