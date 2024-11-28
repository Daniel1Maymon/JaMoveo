from flask_pymongo import ObjectId
from app import mongo

class User:
    @staticmethod
    def find_by_username(username):
        return mongo.db.users.find_one({"username": username})

    @staticmethod
    def create_user(user_data):
        return mongo.db.users.insert_one(user_data)
