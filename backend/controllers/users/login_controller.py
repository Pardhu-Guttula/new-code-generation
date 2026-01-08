from flask import Blueprint, request, jsonify, session
import logging
from backend.services.auth.login_service import LoginService

login_bp = Blueprint("login", __name__)
logger = logging.getLogger(__name__)

def init_login_routes(service: LoginService) -> Blueprint:
    @login_bp.route("/login", methods=["POST"])
    def login() -> tuple:
        data = request.get_json(force=True)
        email = data.get("email")
        password = data.get("password")
        if not email or not password:
            return jsonify({"error": "Email and password are required"}), 400
        try:
            if service.login(email, password):
                session.permanent = True  # To ensure session timeout
                return jsonify({"message": "Login successful"}), 200
            return jsonify({"error": "Invalid email or password"}), 401
        except ValueError as ve:
            logger.warning("Login error: %s", ve)
            return jsonify({"error": str(ve)}), 404
        except PermissionError as pe:
            logger.warning("Account lock error: %s", pe)
            return jsonify({"error": str(pe)}), 403
        except Exception as e:
            logger.error("Unexpected error during login: %s", e)
            return jsonify({"error": "Internal server error"}), 500

    return login_bp