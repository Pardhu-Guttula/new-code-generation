from flask import Blueprint, request, jsonify
from backend.services.cart.cart_service import CartService
from backend.repositories.cart.cart_repository import CartRepository

cart_blueprint = Blueprint('cart', __name__)
cart_repository = CartRepository()
cart_service = CartService(cart_repository)

@cart_blueprint.route('/cart/<int:user_id>', methods=['GET'])
def get_cart(user_id):
    cart = cart_service.get_cart(user_id)
    return jsonify(cart.dict()), 200

@cart_blueprint.route('/cart/<int:user_id>/add', methods=['POST'])
def add_product_to_cart(user_id):
    data = request.json
    product_id = data['product_id']
    quantity = data['quantity']
    cart = cart_service.add_product_to_cart(user_id, product_id, quantity)
    return jsonify(cart.dict()), 201

@cart_blueprint.route('/cart/<int:user_id>/remove', methods=['POST'])
def remove_product_from_cart(user_id):
    data = request.json
    product_id = data['product_id']
    cart = cart_service.remove_product_from_cart(user_id, product_id)
    return jsonify(cart.dict()), 200

@cart_blueprint.route('/cart/<int:user_id>/clear', methods=['POST'])
def clear_cart(user_id):
    cart_service.clear_cart(user_id)
    return jsonify({"message": "Cart cleared"}), 200