from functools import wraps
from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.user_model import User

def admin_required(f):
    @jwt_required()
    @wraps(f)
    def decorated_function(*args, **kwargs):
        current_user = get_jwt_identity()
        print(f"Decoded user: {current_user}")  # Debugging
        
        user = User.find_by_username(username=current_user)
        
        # Extract user role from headers (or another source like JWT)
        # user_role = request.headers.get("Role")
        if user['role'] != "admin":
            return jsonify({"error": "Access denied: Admins only"}), 403
        return f(*args, **kwargs)
    return decorated_function
