from flask import Blueprint, request, jsonify
from app.services.session_service import SessionService
from app.services.auth_service import AuthService
from app.utils.auth import admin_required
from flask_socketio import emit
import traceback
from app import socketio  

session_bp = Blueprint(name='session', import_name=__name__)


@session_bp.route('/start_session', methods=['POST'])
@admin_required
def start_session():
    try:
        current_user = AuthService.get_jwt_identity()
        print(f"Current user: {current_user}") 
        session = SessionService.start_session()
        
        
        socketio.emit("session_started", {"message": "Session has started"}, to='/')
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        
        error_trace = traceback.format_exc()
        print(f"Unexpected error: {error_trace}")
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

    return jsonify({"message": "Session started", "session": session}), 200


@session_bp.route('/create_session', methods=['POST'])
@admin_required
def create_session():
    data = request.json
    name = data.get("name")

    if not name:
        return jsonify({"error": "Session name is required"}), 400

    try:
        session = SessionService.create_session(name, admin_id=request.headers.get("User-ID"))
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred"}), 500

    serialized_session = serialize_session(session)
    return jsonify({"session": serialized_session}), 200


@session_bp.route('/end_session', methods=['POST'])
@admin_required
def end_session():
    data = request.json
    session_id = data.get("session_id")

    if not session_id:
        return jsonify({"error": "Session ID is required"}), 400

    try:
        SessionService.end_session(session_id)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred"}), 500

    return jsonify({"message": "Session ended successfully"}), 200

def serialize_session(session):
    session['_id'] = str(session['_id'])
    session['session_id'] = str(session['session_id'])
    return session

@session_bp.route('/get_active_session', methods=['GET'])
def get_active_session():
    try:
        session = SessionService.get_active_session()
        if not session:
            return jsonify({"error": "No active session found"}), 404
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred"}), 500

    serialized_session = serialize_session(session)
    return jsonify({"session": serialized_session}), 200

