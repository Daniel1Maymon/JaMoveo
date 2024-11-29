from app.models.session_model import Session
import uuid

class SessionService:
    @staticmethod
    def create_session(name, admin_id):
        if Session.get_active_session():
            raise ValueError("An active session already exists")

        session_data = {
            "session_id": str(uuid.uuid4()),
            "name": name,
            "admin_id": admin_id,
            "active": True,
            "selected_song": None,
            "users_connected": []
        }

        try:
            Session.create_session(session_data)
        except Exception as e:
            raise RuntimeError("Failed to create session") from e

        return session_data
    
    
    @staticmethod
    def get_active_session():
        try:
            return Session.get_active_session()
        except Exception as e:
            raise RuntimeError("Failed to fetch active session") from e
        
        
    @staticmethod
    def end_session(session_id):
        session = Session.find_by_id(session_id)
        if not session:
            raise ValueError("Session not found")

        try:
            Session.update_session(session_id, updates={"active": False})
        except Exception as e:
            raise RuntimeError("Failed to end session") from e     