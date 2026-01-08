from flask import Flask
from backend.config.config import Config
from backend.controllers.users.user_controller import user_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    app.register_blueprint(user_blueprint, url_prefix='/api/users')
    
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)