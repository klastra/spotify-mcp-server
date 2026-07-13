import spotipy
import os
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

from database_helper import insert_listening_history, listening_event_exists, query_listening_history, query_most_listened_artists
from parsers import parse_artist, parse_recently_played 

load_dotenv()

mcp = FastMCP("Spotify Music MCP Server")

def get_spotify_client():
    return spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=os.getenv("SPOTIFY_CLIENT_ID"),
            client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
            redirect_uri=os.getenv("SPOTIFY_REDIRECT_URI"),
            scope=[
                "user-top-read",
                "user-read-recently-played"
            ]
        )
    )

#------- MCP TOOLS --------
@mcp.tool()
def fetch_top_artists_from_spotify(limit: int = 10):
    """
    Gets top artists on Spotify.
    Allows Claude to answer "Who are my top 10 artists?"
    """
    spotify = get_spotify_client()
    results = spotify.current_user_top_artists(limit=limit)
    
    artists_parsed = [parse_artist(artist) for artist in results['items']]

    return artists_parsed

@mcp.tool()
def fetch_recently_played_from_spotify(limit: int = 10):
    """
    Gets recently played songs on Spotify.
    Allows Claude to answer "What songs have I listened to recently?"
    """
    spotify = get_spotify_client()
    results = spotify.current_user_recently_played(limit=limit)
    
    songs_parsed = [parse_recently_played(song) for song in results['items']]

    return songs_parsed

@mcp.tool()
def sync_recently_played():
    """
    Syncs recently played songs into the database.
    Checks if song being inserted already exists in the database before inserting.
    Returns the count of new listening events.
    """
    recent_tracks = fetch_recently_played_from_spotify()
    new_listens = 0

    for track in recent_tracks:
        if not listening_event_exists(track['track_id'], track['played_at']):
            insert_listening_history(track)
            new_listens += 1
    return {
        "status":"success",
        "message": f"Inserted {new_listens} new listening event(s)!"
    }

@mcp.tool()
def get_listening_history(limit: int = 50):
    """
    Gets listening history from the local database.
    This is used for analyzing listening patterns.
    """
    return query_listening_history(limit)

@mcp.tool()
def get_most_played_artists(limit: int = 10):
    """
    Gets most played artists based on history.
    Answers "Among the listening events I've collected, who appears most often?"
    """
    return query_most_listened_artists(limit)

if __name__ == "__main__":
    mcp.run()