from flask import Flask
from digital_banking_portal.backend.config.config import DevelopmentConfig
from digital_banking_portal.backend.models import db

def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app

if __name__ == "__main__":
    app = create_app()
    app.run()