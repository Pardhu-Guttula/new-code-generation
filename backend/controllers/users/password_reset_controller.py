from flask import Blueprint, jsonify, request
import logging
from backend.services.auth.password_reset_service import PasswordResetService

password_reset_bp = Blueprint("password_reset", __name__)
logger = logging.getLogger(__name__)

def init_password_reset_routes(service: PasswordResetService) -> Blueprint:
    @password_reset_bp.route("/password-reset/initiate", methods=["POST"])
    def initiate_reset() -> tuple:
        data = request.get_json(force=True)
        email = data.get("email")
        if not email:
            return jsonify({"error": "Email is required"}), 400
        try:
            reset_info = service.initiate_reset(email)
            return jsonify({"token": reset_info.token, "expires_at": reset_info.expires_at}), 200
        except ValueError as ve:
            logger.warning("Password reset initiation failed: %s", ve)
            return jsonify({"error": str(ve)}), 400
        except Exception as e:
            logger.error("Unexpected error initiating password reset: %s", e)
            return jsonify({"error": "Internal server error"}), 500

    @password_reset_bp.route("/password-reset/confirm", methods=["POST"])
    def reset_password() -> tuple:
        data = request.get_json(force=True)
        token = data.get("token")
        new_password = data.get("new_password")
        if not token or not new_password:
            return jsonify({"error": "Token and new password are required"}), 400
        try:
            service.reset_password(token, new_password)
            return jsonify({"message": "Password reset successful"}), 200
        except ValueError as ve:
            logger.warning("Password reset failed: %s", ve)
            return jsonify({"error": str(ve)}), 400
        except Exception as e:
            logger.error("Unexpected error resetting password: %s", e)
            return jsonify({"error": "Internal server error"}), 500

    return password_reset_bp