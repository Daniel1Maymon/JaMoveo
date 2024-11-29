from flask import Flask
from flask_pymongo import PyMongo
from config.config import Config

mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize MongoDB
    mongo.init_app(app)

    # Register Blueprints
    from app.controllers.auth_controller import auth_bp
    from app.controllers.session_controller import session_bp
    
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(session_bp, url_prefix="/session")

    return app
