import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    # SECRET_KEY = secrets.token_hex(32)
    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")
    
    
    
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/defaultdb")
    

    # MONGO_URI = "mongodb+srv://<username>:<password>@<cluster-name>.mongodb.net/<DB_name>"

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SONGS_DIR = os.path.join(BASE_DIR, '../app/songs')
    SONGS_FOLDER = os.path.abspath(SONGS_DIR)