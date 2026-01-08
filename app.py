from flask import Flask
from flask_socketio import SocketIO, emit
from backend.controllers.users.notification_controller import notification_controller

socketio = SocketIO()

def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(notification_controller, url_prefix='/user')
    socketio.init_app(app)
    return app

@socketio.on('connect')
def handle_connect():
    emit('message', {'message': 'Connected successfully'})

if __name__ == '__main__':
    app = create_app()
    socketio.run(app, host='0.0.0.0', port=5000)