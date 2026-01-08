from flask import Blueprint, request, jsonify
import logging
from backend.services.cart.cart_service import CartService

cart_bp = Blueprint("cart", __name__)
logger = logging.getLogger(__name__)

def init_cart_routes(service: CartService) -> Blueprint:
    @cart_bp.route("/add", methods=["POST"])
    def add_to_cart() -> tuple:
        data = request.get_json(force=True)
        user_id = data.get("user_id")
        product_id = data.get("product_id")
        quantity = data.get("quantity")

        if user_id is None or product_id is None or quantity is None:
            return jsonify({"error": "User ID, Product ID, and Quantity are required fields"}), 400

        try:
            cart = service.add_to_cart(user_id, product_id, quantity)
            return jsonify({
                "user_id": cart.user_id,
                "items": [{
                    "product_id": item.product_id,
                    "quantity": item.quantity
                } for item in cart.items]
            }), 200
        except ValueError as ve:
            logger.warning("Adding to cart failed: %s", ve)
            return jsonify({"error": str(ve)}), 400
        except Exception as e:
            logger.error("Unexpected error adding to cart: %s", e)
            return jsonify({"error": "Internal server error"}), 500

    return cart_bp