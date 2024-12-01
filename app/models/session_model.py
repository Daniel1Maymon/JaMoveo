from app import mongo

class Session:
    @staticmethod
    def create_or_update_session(session_data):
        # Update or create a session with _id = "session"
        updated_session = mongo.db.sessions.update_one(
            {"_id": "session"},  # Find a document with _id = "session"
            {"$set": session_data},  # Update the document
            upsert=True  # Create a new document if it doesn't exist
        )
        
        # return updated_session

    @staticmethod
    def find_by_id(session_id):
        return mongo.db.sessions.find_one({"_id": session_id})

    @staticmethod
    def update_session(session_id, updates):
        return mongo.db.sessions.update_one({"_id": session_id}, {"$set": updates})

    @staticmethod
    def get_active_session():
        return mongo.db.sessions.find_one({"active": True})
