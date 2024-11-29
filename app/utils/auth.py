from functools import wraps
from flask import request, jsonify

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Extract user role from headers (or another source like JWT)
        user_role = request.headers.get("Role")
        if user_role != "admin":
            return jsonify({"error": "Access denied: Admins only"}), 403
        return f(*args, **kwargs)
    return decorated_function
