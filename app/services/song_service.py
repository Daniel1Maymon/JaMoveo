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
            return Song.search_by_query(query)
        except Exception as e:
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