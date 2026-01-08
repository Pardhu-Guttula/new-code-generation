from flask import Blueprint, request, jsonify
from backend.services.product_catalog.product_service import ProductService
from backend.repositories.products.product_repository import ProductRepository

product_blueprint = Blueprint('product', __name__)
product_repository = ProductRepository()
product_service = ProductService(product_repository)

@product_blueprint.route('/products', methods=['POST'])
def add_product():
    data = request.json
    product = product_service.add_product(data)
    return jsonify(product.dict()), 201

@product_blueprint.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.json
    product = product_service.update_product(product_id, data)
    return jsonify(product.dict()), 200

@product_blueprint.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = product_service.get_product(product_id)
    return jsonify(product.dict()), 200

@product_blueprint.route('/products', methods=['GET'])
def list_products():
    products = product_service.list_products()
    return jsonify([product.dict() for product in products]), 200

@product_blueprint.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    # You may want to add additional authentication check to ensure only admins can delete products
    confirmation = request.json.get('confirmation')
    if confirmation != 'yes':
        return jsonify({"error": "Product deletion not confirmed"}), 400
    product_service.delete_product(product_id)
    return jsonify({"message": "Product deleted"}), 200

@product_blueprint.route('/products/search', methods=['GET'])
def search_products():
    query = request.args.get('query', '')
    page = int(request.args.get('page', 1))
    page_size = int(request.args.get('page_size', 10))
    products = product_service.search_products(query, page, page_size)
    return jsonify([product.dict() for product in products]), 200