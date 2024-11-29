from flask import Flask, json
from flask_pymongo import PyMongo
from app.utils.initializations import load_songs_from_folder
from config.config import Config

mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize MongoDB
    mongo.init_app(app)
    
    # Load songs from MongoDB
    load_songs_from_folder()

    # Register Blueprints
    from app.controllers.auth_controller import auth_bp
    from app.controllers.session_controller import session_bp
    from app.controllers.song_controller import song_bp
    
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(session_bp, url_prefix="/session")
    app.register_blueprint(song_bp, url_prefix='/song')
    

    return app
