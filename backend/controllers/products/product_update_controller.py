from flask import Blueprint, request, jsonify
import logging
from backend.services.product_catalog.product_update_service import ProductUpdateService

product_update_bp = Blueprint("product_update", __name__)
logger = logging.getLogger(__name__)

def init_product_update_routes(service: ProductUpdateService) -> Blueprint:
    @product_update_bp.route("/<int:product_id>/update", methods=["PUT"])
    def update_product(product_id: int) -> tuple:
        data = request.get_json(force=True)
        name = data.get("name")
        description = data.get("description")
        price = data.get("price")
        if not name or not description or price is None:
            return jsonify({"error": "All fields (name, description, price) are required"}), 400
        try:
            product = service.update_product(product_id, name, description, price)
            return jsonify({"id": product.id, "name": product.name, "description": product.description, "price": product.price, "category_id": product.category_id}), 200
        except ValueError as ve:
            logger.warning("Product update failed: %s", ve)
            return jsonify({"error": str(ve)}), 404
        except Exception as e:
            logger.error("Unexpected error updating product: %s", e)
            return jsonify({"error": "Internal server error"}), 500

    return product_update_bp