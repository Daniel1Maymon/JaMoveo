import os
from dotenv import load_dotenv
# load_dotenv()
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../.env'))

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")

    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/defaultdb")

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SONGS_DIR = os.path.join(BASE_DIR, '../app/songs')
    SONGS_FOLDER = os.path.abspath(SONGS_DIR)

    print(f"SECRET_KEY = {SECRET_KEY}")
    print(f"MONGO_URI = {MONGO_URI}")
    print(f"BASE_DIR = {BASE_DIR}")
    print(f"SONGS_DIR = {SONGS_DIR}")
    print(f"SONGS_FOLDER = {SONGS_FOLDER}")
    print(f"TEST_VAR = {TEST_VAR}")