import logging
from flask import Flask
from flask.sessions import SecureCookieSessionInterface
from flask_session import Session
from backend.config.settings import settings
from backend.repositories.cart.shopping_cart_repository import ShoppingCartRepository
from backend.services.cart.cart_service import CartService
from backend.controllers.cart.cart_controller import init_cart_routes

def create_app() -> Flask:
    app = Flask(__name__)
    app.config["SECRET_KEY"] = settings.SECRET_KEY
    app.config["SESSION_TYPE"] = "filesystem"

    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")

    Session(app)  # Enabling server-side session management

    cart_repo = ShoppingCartRepository(settings.DATABASE_PATH)
    cart_service = CartService(cart_repo)

    app.register_blueprint(init_cart_routes(cart_service), url_prefix="/api/cart")

    @app.route("/health", methods=["GET"])
    def health() -> dict:
        return {"status": "healthy"}

    return app

if __name__ == "__main__":
    application = create_app()
    application.run(debug=settings.DEBUG)