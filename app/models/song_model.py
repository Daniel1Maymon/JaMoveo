from app import mongo
from bson.objectid import ObjectId

class Song:
    @staticmethod
    def get_songs():
        songs = mongo.db.songs.find({}, {"_id": 1, "title": 1, "content": 1})
        
        return [
            {
                **song,
                "_id": str(song["_id"])
            }
            for song in songs
        ]
    
    @staticmethod
    def search_by_query(query):
        regex = {"$regex": query, "$options": "i"}
        songs = mongo.db.songs.find(
            {"title": regex},
            {"title": 1}
        )
        return [
            {"id": str(song["_id"]), "title": song["title"]}
            for song in songs
        ]
        
    @staticmethod
    def find_by_id(song_id):
        return mongo.db.songs.find_one({"_id": ObjectId(song_id)})
    