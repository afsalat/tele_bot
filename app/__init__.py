from flask import Flask
from config import Config
from .models import init_db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize the database
    init_db(app)

    with app.app_context():
        from .handler import bp_handler
        from .api import api_bp
        app.register_blueprint(bp_handler)
        app.register_blueprint(api_bp, url_prefix='/api')

    return app
