from app import mongo
from bson.objectid import ObjectId

class Song:
    @staticmethod
    def get_songs():
        # Fetch songs from MongoDB
        songs = mongo.db.songs.find({}, {"_id": 1, "title": 1, "content": 1})
        
        # Convert ObjectId to string for each song
        return [
            {
                **song,
                "_id": str(song["_id"])  # Convert ObjectId to string
            }
            for song in songs
        ]
    
    @staticmethod
    def search_by_query(query):
        return list(mongo.db.songs.find(
            {"$or": [
                {"title": {"$regex": query, "$options": "i"}},
                {"artist": {"$regex": query, "$options": "i"}}
            ]},
            {"_id": 0}
        ))
        
    @staticmethod
    def find_by_id(song_id):
        return mongo.db.songs.find_one({"_id": ObjectId(song_id)})
    