import logging
from flask import Flask
from flask.sessions import SecureCookieSessionInterface
from flask_session import Session
from backend.config.settings import settings
from backend.repositories.users.user_repository import UserRepository
from backend.services.user_management.profile_service import ProfileService
from backend.controllers.users.profile_controller import init_profile_routes

def create_app() -> Flask:
    app = Flask(__name__)
    app.config["SECRET_KEY"] = settings.SECRET_KEY
    app.config["SESSION_TYPE"] = "filesystem"
    
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")

    Session(app)  # Enabling server-side session management

    user_repo = UserRepository(settings.DATABASE_PATH)
    profile_service = ProfileService(user_repo)

    app.register_blueprint(init_profile_routes(profile_service), url_prefix="/api/users")

    @app.route("/health", methods=["GET"])
    def health() -> dict:
        return {"status": "healthy"}

    return app

if __name__ == "__main__":
    application = create_app()
    application.run(debug=settings.DEBUG)