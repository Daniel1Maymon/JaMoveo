from flask import Blueprint, request, jsonify
from app.services.song_service import SongService
from app.utils.auth import admin_required

song_bp = Blueprint(name='song', import_name=__name__)

@song_bp.route('/songs', methods=['GET'])
def get_songs():
    songs = SongService.get_all_songs()
    return jsonify(songs), 200


@song_bp.route('/search_songs', methods=['POST'])
def search_songs():
    try:
        # Get the search query from the request body
        query = request.json.get('query', '').strip()
        
        # Validate that query is not empty
        if not query:
            raise ValueError("Search query cannot be empty.")

        # Call the service layer to search for songs
        songs = SongService.search_songs(query)

        # Return the results
        return jsonify(songs), 200
    except ValueError as e:
        # Return an error response for invalid inputs
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        # Handle any other unexpected errors
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

    
@song_bp.route('/select_song', methods=['POST'])
@admin_required
def select_song():
    try:
        # Extract song_id from the request
        song_id = request.json.get('song_id')
        if not song_id:
            return jsonify({"error": "song_id is required"}), 400
        
        # Call the service layer to select the song
        song = SongService.select_song(song_id)
        song['_id'] = str(song['_id'])
        return jsonify({"message": "Song selected successfully", "song": song}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": "An error occurred"}), 500