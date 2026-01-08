from flask import Flask
from backend.controllers.data.data_controller import data_controller

def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(data_controller, url_prefix='/data')
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000)