import logging
from flask import Flask
from flask.sessions import SecureCookieSessionInterface
from flask_session import Session
from backend.config.settings import settings
from backend.repositories.products.product_repository import ProductRepository
from backend.services.product_catalog.product_update_service import ProductUpdateService
from backend.controllers.products.product_update_controller import init_product_update_routes

def create_app() -> Flask:
    app = Flask(__name__)
    app.config["SECRET_KEY"] = settings.SECRET_KEY
    app.config["SESSION_TYPE"] = "filesystem"

    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")

    Session(app)  # Enabling server-side session management

    product_repo = ProductRepository(settings.DATABASE_PATH)
    product_update_service = ProductUpdateService(product_repo)

    app.register_blueprint(init_product_update_routes(product_update_service), url_prefix="/api/products")

    @app.route("/health", methods=["GET"])
    def health() -> dict:
        return {"status": "healthy"}

    return app

if __name__ == "__main__":
    application = create_app()
    application.run(debug=settings.DEBUG)