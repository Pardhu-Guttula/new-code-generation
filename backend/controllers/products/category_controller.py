from flask import Blueprint, request, jsonify
import logging
from backend.services.product_catalog.category_service import CategoryService

category_bp = Blueprint("category", __name__)
logger = logging.getLogger(__name__)

def init_category_routes(service: CategoryService) -> Blueprint:
    @category_bp.route("/add", methods=["POST"])
    def add_category() -> tuple:
        data = request.get_json(force=True)
        name = data.get("name")
        description = data.get("description")
        parent_id = data.get("parent_id")
        if not name or not description:
            return jsonify({"error": "All fields (name, description) are required"}), 400
        try:
            category = service.create_category(name, description, parent_id)
            return jsonify({
                "id": category.id,
                "name": category.name,
                "description": category.description,
                "parent_id": category.parent_id,
                "created_at": category.created_at,
                "updated_at": category.updated_at,
            }), 201
        except ValueError as ve:
            logger.warning("Category creation failed: %s", ve)
            return jsonify({"error": str(ve)}), 400
        except Exception as e:
            logger.error("Unexpected error creating category: %s", e)
            return jsonify({"error": "Internal server error"}), 500

    @category_bp.route("/list", methods=["GET"])
    def list_categories() -> tuple:
        try:
            categories = service.get_all_categories()
            return jsonify([{
                "id": category.id,
                "name": category.name,
                "description": category.description,
                "parent_id": category.parent_id,
                "created_at": category.created_at,
                "updated_at": category.updated_at,
            } for category in categories]), 200
        except Exception as e:
            logger.error("Unexpected error listing categories: %s", e)
            return jsonify({"error": "Internal server error"}), 500

    return category_bp