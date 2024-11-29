import os
import json

from config.config import Config

def load_songs_from_folder():
    # Get the path to the songs folder from the app config
    songs_folder = Config.SONGS_FOLDER
    from app import mongo
    songs_collection = mongo.db.songs

    # Ensure the folder exists
    if not os.path.exists(songs_folder):
        print(f"Songs folder does not exist: {songs_folder}")
        return

    # Iterate over all JSON files in the folder
    for filename in os.listdir(songs_folder):
        if filename.endswith('.json'):
            file_path = os.path.join(songs_folder, filename)
            try:
                with open(file_path, 'r') as file:
                    song_content = json.load(file)  # Load the file content
                                    # Add metadata to the song
                    song_document = {
                        "title": filename.split('.json')[0].replace('_', ' '),  # Song title based on the filename
                        "content": song_content  # The JSON content as is
                    }
                    
                    # Check if the song already exists in the database
                    existing_song = songs_collection.find_one({"title": song_document["title"]})
                    if not existing_song:
                        songs_collection.insert_one(song_document)
                        print(f"Inserted song: {song_document['title']}")
                    else:
                        print(f"Song already exists: {song_document['title']}")
                        
            except Exception as e:
                print(f"Error loading file {file_path}: {e}")
