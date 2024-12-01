from flask import Flask, json
from flask_pymongo import PyMongo
from app.utils.initializations import load_songs_from_folder
from config.config import Config
from flask_cors import CORS
from datetime import timedelta
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_socketio import SocketIO



mongo = PyMongo()
socketio = SocketIO(cors_allowed_origins="*", async_mode="threading")

def create_app():
    app = Flask(__name__)
    CORS(app) 
    
    app.config.from_object(Config)
    app.config['JWT_SECRET_KEY'] = Config.SECRET_KEY
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)  # Token expiration set to 1 hour
    
    # Initialize MongoDB
    mongo.init_app(app)
    
    jwt = JWTManager(app)  # Initialize JWT Manager
    
    # Load songs from MongoDB
    load_songs_from_folder()

    # Register Blueprints
    from app.controllers.auth_controller import auth_bp
    from app.controllers.session_controller import session_bp
    from app.controllers.song_controller import song_bp
    
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(session_bp, url_prefix="/session")
    app.register_blueprint(song_bp, url_prefix='/song')

    # Initialize SocketIO with the app
    socketio.init_app(app)  # Link socketio to the app

    return app
