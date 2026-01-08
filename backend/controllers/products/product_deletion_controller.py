from flask import Blueprint, request, jsonify
import logging
from backend.services.product_catalog.product_deletion_service import ProductDeletionService

product_deletion_bp = Blueprint("product_deletion", __name__)
logger = logging.getLogger(__name__)

def init_product_deletion_routes(service: ProductDeletionService) -> Blueprint:
    @product_deletion_bp.route("/<int:product_id>/delete", methods=["DELETE"])
    def delete_product(product_id: int) -> tuple:
        try:
            service.delete_product(product_id)
            return jsonify({"message": "Product deleted successfully"}), 200
        except ValueError as ve:
            logger.warning("Product deletion failed: %s", ve)
            return jsonify({"error": str(ve)}), 404
        except Exception as e:
            logger.error("Unexpected error deleting product: %s", e)
            return jsonify({"error": "Internal server error"}), 500

    return product_deletion_bp