from flask import Blueprint, request, jsonify

from app.services.auth_service import AuthService
from flask_jwt_extended import jwt_required
auth_bp = Blueprint(name='auth', import_name=__name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    instrument = data.get('instrument')

    if not username or not password or not instrument:
        return jsonify({"error": "Missing required fields"}), 400

    try:
        AuthService.register_user(username, password, instrument, "player")
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    return jsonify({"message": "User registered successfully"}), 201


@auth_bp.route('/admin_register', methods=['POST'])
def admin_register():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    instrument = data.get('instrument')

    if not username or not password or not instrument:
        return jsonify({"error": "Missing required fields"}), 400

    try:
        AuthService.register_user(username, password, instrument, "admin")
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    return jsonify({"message": "Admin registered successfully"}), 201


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    try:
        result = AuthService.login_user(username, password)
        token = result["token"]
        role = result["role"]
    except ValueError as e:
        return jsonify({"error": str(e)}), 401

    return jsonify({"token": token, "role": role}), 200


@auth_bp.route('/protected', methods=['GET'])
@jwt_required() 
def protected():
    
    current_user = AuthService.get_jwt_identity()
    return jsonify({"message": "Welcome!", "user": current_user}), 200

@auth_bp.route('/admin-only', methods=['GET'])
@jwt_required() 
def admin_only():
    
    current_user = AuthService.get_jwt_identity()
    print(f"current_user: \n{current_user}")
    
    
    if current_user['role'] != 'admin':
        return jsonify({"error": "Access denied"}), 403
    return jsonify({"message": "Welcome, Admin!"}), 200