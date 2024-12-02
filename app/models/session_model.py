from app import mongo

class Session:
    @staticmethod
    def create_or_update_session(session_data):
        updated_session = mongo.db.sessions.update_one(
            {"_id": "session"}, 
            {"$set": session_data}, 
            upsert=True 
        )
        

    @staticmethod
    def find_by_id(session_id):
        return mongo.db.sessions.find_one({"_id": session_id})

    @staticmethod
    def update_session(session_id, updates):
        return mongo.db.sessions.update_one({"_id": session_id}, {"$set": updates})

    @staticmethod
    def get_active_session():
        return mongo.db.sessions.find_one({"active": True})
