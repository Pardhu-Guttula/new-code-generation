from flask import Flask
from backend.controllers.auth.auth_controller import auth_controller
from backend.controllers.accounts.account_controller import account_controller
from backend.controllers.notifications.notification_controller import notification_controller

def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(auth_controller, url_prefix='/auth')
    app.register_blueprint(account_controller, url_prefix='/api')
    app.register_blueprint(notification_controller, url_prefix='/api')
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000)