from flask import Blueprint, render_template

responsive_controller = Blueprint('responsive_controller', __name__)

@responsive_controller.route('/')
def index():
    return render_template('index.html')

@responsive_controller.route('/products')
def products():
    return render_template('products.html')

@responsive_controller.route('/cart')
def cart():
    return render_template('cart.html')