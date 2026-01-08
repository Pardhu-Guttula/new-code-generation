from flask import Blueprint, request, jsonify
from backend.services.auth.auth_service.py import AuthService

user_blueprint = Blueprint('user', __name__)
auth_service = AuthService()

@user_blueprint.route('/register', methods=['POST'])
def register():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    user = auth_service.register_user(email, password)
    return jsonify(user.dict()), 201