from flask import Flask
from backend.controllers.sync.sync_controller import sync_controller

def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(sync_controller, url_prefix='/api')
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000)