from flask import Blueprint, request, jsonify
import logging
from backend.services.product_catalog.product_search_service import ProductSearchService

product_search_bp = Blueprint("product_search", __name__)
logger = logging.getLogger(__name__)

def init_product_search_routes(service: ProductSearchService) -> Blueprint:
    @product_search_bp.route("/search", methods=["GET"])
    def search_products() -> tuple:
        query = request.args.get("query", "")
        category_id = request.args.get("category_id", type=int)
        page = request.args.get("page", 1, type=int)
        per_page = request.args.get("per_page", 10, type=int)

        if not query:
            return jsonify({"error": "Query parameter is required"}), 400

        try:
            products = service.search_products(query, category_id, page, per_page)
            return jsonify([{
                "id": product.id,
                "name": product.name,
                "description": product.description,
                "price": product.price,
                "category_id": product.category_id,
                "is_deleted": product.is_deleted,
                "created_at": product.created_at,
                "updated_at": product.updated_at
            } for product in products]), 200
        except Exception as e:
            logger.error("Unexpected error in product search: %s", e)
            return jsonify({"error": "Internal server error"}), 500

    return product_search_bp