from app import mongo

class Session:
    @staticmethod
    def create_session(session_data):
        return mongo.db.sessions.insert_one(session_data)

    @staticmethod
    def find_by_id(session_id):
        return mongo.db.sessions.find_one({"session_id": session_id})

    @staticmethod
    def update_session(session_id, updates):
        return mongo.db.sessions.update_one({"session_id": session_id}, {"$set": updates})

    @staticmethod
    def get_active_session():
        return mongo.db.sessions.find_one({"active": True})
