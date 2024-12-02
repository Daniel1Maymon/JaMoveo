import bcrypt
import jwt
from datetime import datetime, timedelta
from config.config import Config
from app.models.user_model import User
from flask_jwt_extended import get_jwt_identity


class AuthService:
    @staticmethod
    def register_user(username, password, instrument, role):
        if User.find_by_username(username):
            raise ValueError("Username already exists")

        hashed_password = AuthService.hash_password(password)
        user_data = {
            "username": username,
            "password": hashed_password,
            "instrument": instrument,
            "role": role
        }
        User.create_user(user_data)


    @staticmethod
    def login_user(username, password):
        user = User.find_by_username(username)
        if not user or not AuthService.verify_password(password, user['password']):
            raise ValueError("Invalid credentials")

        token = AuthService.generate_jwt({
            "id": str(user['_id']),
            "username": username,
            "role": user["role"] 
        })
        
        print(f"Generated JWT: {token}")
        
        return {"token": token, "role": user["role"]}


    @staticmethod
    def verify_password(password, hashed_password):
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

    @staticmethod
    def generate_jwt(payload):
        payload['sub'] = payload.get('username')
        payload['exp'] = datetime.utcnow() + timedelta(hours=1)
        return jwt.encode(payload, Config.SECRET_KEY, algorithm='HS256')

    @staticmethod
    def hash_password(password):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    @staticmethod
    def get_jwt_identity():
        return get_jwt_identity()