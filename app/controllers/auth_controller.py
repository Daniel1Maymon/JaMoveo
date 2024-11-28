from flask import Blueprint, request, jsonify
from app.models.user_model import User
from app.services.auth_service import AuthService

auth_bp = Blueprint(name='auth', import_name=__name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    instrument = data.get('instrument')

    if not username or not password or not instrument:
        return jsonify({"error": "Missing required fields"}), 400

    if User.find_by_username(username):
        return jsonify({"error": "Username already exists"}), 400

    hashed_password = AuthService.hash_password(password)
    User.create_user(user_data={
        "username": username,
        "password": hashed_password,
        "instrument": instrument,
        "role": "player"  
    })
    return jsonify({"message": "user registered successfully"}), 201


@auth_bp.route('/admin_register', methods=['POST'])
def admin_register():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    instrument = data.get('instrument')
    
    if not username or not password or not instrument:
        return jsonify({"error": "Missing required fields"}), 400

    if User.find_by_username(username):
        return jsonify({"error": "Username already exists"}), 400
    
    hashed_password = AuthService.hash_password(password)
    
    User.create_user(user_data={
        "username": username,
        "password": hashed_password,
        "instrument": instrument,
        "role": "admin"  
    })
    return jsonify({"message": "Admin registered successfully"}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    user = User.find_by_username(username)
    if not user or not AuthService.verify_password(password, user['password']):
        return jsonify({"error": "Invalid credentials"}), 401

    token = AuthService.generate_jwt({"id": str(user['_id']), "username": username})
    return jsonify({"token": token}), 200
