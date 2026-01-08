from flask import Flask
from backend.controllers.users.dashboard_controller import dashboard_controller

def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(dashboard_controller, url_prefix='/user')
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000)