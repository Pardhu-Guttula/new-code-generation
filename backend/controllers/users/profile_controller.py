from flask import Blueprint, jsonify, request
import logging
from backend.services.user_management.profile_service import ProfileService

profile_bp = Blueprint("profile", __name__)
logger = logging.getLogger(__name__)

def init_profile_routes(service: ProfileService) -> Blueprint:
    @profile_bp.route("/<int:user_id>/update", methods=["PUT"])
    def update_profile(user_id: int) -> tuple:
        data = request.get_json(force=True)
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        phone_number = data.get("phone_number")
        if not first_name or not last_name or not phone_number:
            return jsonify({"error": "All fields (first_name, last_name, phone_number) are required"}), 400
        try:
            user = service.update_profile(user_id, first_name, last_name, phone_number)
            return jsonify({"id": user.id, "email": user.email, "first_name": user.first_name, "last_name": user.last_name, "phone_number": user.phone_number}), 200
        except ValueError as ve:
            logger.warning("Profile update failed: %s", ve)
            return jsonify({"error": str(ve)}), 404
        except Exception as e:
            logger.error("Unexpected error updating profile: %s", e)
            return jsonify({"error": "Internal server error"}), 500

    return profile_bp