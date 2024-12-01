import traceback
from app.models.song_model import Song # type: ignore

class SongService:
    @staticmethod
    def get_all_songs():
        try:
            return Song.get_songs()
        except Exception as e:
            raise RuntimeError("Failed to fetch songs") from e
        
    @staticmethod
    def search_songs(query):
        if not query:
            raise ValueError("Query parameter is required")
        
        try:
            # Call the model layer to perform the query
            return Song.search_by_query(query)
        except Exception as e:
            # Log the full traceback for debugging
            error_trace = traceback.format_exc()
            print(f"Unexpected error: {error_trace}")
            # Raise a runtime error with a descriptive message
            raise RuntimeError("Failed to search songs") from e
    
    @staticmethod
    def select_song(song_id):
        try:
            # Fetch the song using the model
            song = Song.find_by_id(song_id)
            if not song:
                raise ValueError("Song not found")
            return song
        except ValueError as e:
            raise  # Pass the ValueError up to the Controller
        except Exception as e:
            raise RuntimeError("Failed to select song") from e