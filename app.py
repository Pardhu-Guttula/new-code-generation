import logging
from flask import Flask
from flask.sessions import SecureCookieSessionInterface
from flask_session import Session
from backend.config.settings import settings
from backend.repositories.products.category_repository import CategoryRepository
from backend.services.product_catalog.category_service import CategoryService
from backend.controllers.products.category_controller import init_category_routes

def create_app() -> Flask:
    app = Flask(__name__)
    app.config["SECRET_KEY"] = settings.SECRET_KEY
    app.config["SESSION_TYPE"] = "filesystem"

    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")

    Session(app)  # Enabling server-side session management

    category_repo = CategoryRepository(settings.DATABASE_PATH)
    category_service = CategoryService(category_repo)

    app.register_blueprint(init_category_routes(category_service), url_prefix="/api/categories")

    @app.route("/health", methods=["GET"])
    def health() -> dict:
        return {"status": "healthy"}

    return app

if __name__ == "__main__":
    application = create_app()
    application.run(debug=settings.DEBUG)