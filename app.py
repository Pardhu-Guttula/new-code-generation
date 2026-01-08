from flask import Flask
from backend.controllers.ui.responsive_controller import responsive_controller

def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(responsive_controller)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000)

=====
FILE 3
=====
Path: requirements.txt
Flask==2.3.2
jinja2==3.1.2

**NOTE**: 

Since the implementation of adaptive designs primarily resides within front-end code (HTML/CSS with media queries, JavaScript for dynamic behaviors), more context would be needed for a full implementation, which should likely include actual template files (index.html, products.html, cart.html) with responsive design considerations (e.g., Bootstrap framework or custom CSS with media queries). The current scope seems restricted in the context of the folder structure provided.