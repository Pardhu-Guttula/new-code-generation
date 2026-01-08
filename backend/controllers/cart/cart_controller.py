from flask import Blueprint, request, jsonify
from backend.services.cart.cart_service import CartService
from backend.repositories.cart.cart_repository import CartRepository

cart_blueprint = Blueprint('cart', __name__)
cart_repository = CartRepository()
cart_service = CartService(cart_repository)

@cart_blueprint.route('/cart/<int:user_id>', methods=['GET'])
def get_cart(user_id):
    cart = cart_service.get_cart(user_id)
    # Calculate total price within this endpoint or create another function in CartService for calculating the total price.
    total_price = sum(item.quantity * product_service.get_product(item.product_id).price for item in cart.items)
    response_data = cart.dict()
    response_data['total_price'] = total_price
    return jsonify(response_data), 200

@cart_blueprint.route('/cart/<int:user_id>/add', methods=['POST'])
def add_product_to_cart(user_id):
    data = request.json
    product_id = data['product_id']
    quantity = data['quantity']
    cart = cart_service.add_product_to_cart(user_id, product_id, quantity)
    return jsonify(cart.dict()), 201

@cart_blueprint.route('/cart/<int:user_id>/remove', methods=['POST'])
def remove_product_from_cart(user_id):
    confirmation = request.json.get('confirmation')
    if confirmation != 'yes':
        return jsonify({"error": "Product removal not confirmed"}), 400

    data = request.json
    product_id = data['product_id']
    cart = cart_service.remove_product_from_cart(user_id, product_id)
    return jsonify(cart.dict()), 200

@cart_blueprint.route('/cart/<int:user_id>/modify', methods=['POST'])
def modify_product_quantity(user_id):
    data = request.json
    product_id = data['product_id']
    quantity = data['quantity']
    cart = cart_service.modify_product_quantity(user_id, product_id, quantity)
    total_price = sum(item.quantity * product_service.get_product(item.product_id).price for item in cart.items)
    response_data = cart.dict()
    response_data['total_price'] = total_price
    return jsonify(response_data), 200

@cart_blueprint.route('/cart/<int:user_id>/clear', methods=['POST'])
def clear_cart(user_id):
    cart_service.clear_cart(user_id)
    return jsonify({"message": "Cart cleared"}), 200