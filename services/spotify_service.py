from database.database_helper import insert_listening_history, listening_event_exists
from parsers.parsers import parse_artist, parse_recently_played
from spotify.spotify_client import get_spotify_client

# Spotify API Calls
def fetch_top_artists_from_spotify(limit: int = 10) -> list[dict]:
    spotify = get_spotify_client()
    results = spotify.current_user_top_artists(limit=limit)
    
    artists_parsed = [parse_artist(artist) for artist in results['items']]

    return artists_parsed


def fetch_recently_played_from_spotify(limit: int = 10) -> list[dict]:
    spotify = get_spotify_client()
    results = spotify.current_user_recently_played(limit=limit)
    
    songs_parsed = [parse_recently_played(song) for song in results['items']]

    return songs_parsed

def sync_recently_played() -> dict:
    recent_tracks = fetch_recently_played_from_spotify()
    new_listens = 0

    for track in recent_tracks:
        if not listening_event_exists(track['track_id'], track['played_at']):
            insert_listening_history(track)
            new_listens += 1
    return {
        "status":"success",
        "inserted": new_listens,
        "message": f"Inserted {new_listens} new listening event(s)!"
    }