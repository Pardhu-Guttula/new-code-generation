from flask import Blueprint, request, jsonify
import logging
from backend.services.product_catalog.product_creation_service import ProductCreationService

product_creation_bp = Blueprint("product_creation", __name__)
logger = logging.getLogger(__name__)

def init_product_creation_routes(service: ProductCreationService) -> Blueprint:
    @product_creation_bp.route("/add", methods=["POST"])
    def add_product() -> tuple:
        data = request.get_json(force=True)
        name = data.get("name")
        description = data.get("description")
        price = data.get("price")
        category_id = data.get("category_id")
        if not name or not description or price is None or category_id is None:
            return jsonify({"error": "All fields (name, description, price, category_id) are required"}), 400
        try:
            product = service.create_product(name, description, price, category_id)
            return jsonify({"id": product.id, "name": product.name, "description": product.description, "price": product.price, "category_id": product.category_id}), 201
        except ValueError as ve:
            logger.warning("Product creation failed: %s", ve)
            return jsonify({"error": str(ve)}), 400
        except Exception as e:
            logger.error("Unexpected error creating product: %s", e)
            return jsonify({"error": "Internal server error"}), 500

    return product_creation_bp