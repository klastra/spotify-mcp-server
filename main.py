import spotipy
import os
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth 

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

def parse_artist(artist: dict) -> dict:
    return {
        "id": artist["id"],
        "name": artist["name"]
    }

def parse_recently_played(item: dict) -> dict:
    track = item["track"]

    return {
        "track_id": track["id"],
        "track_name": track["name"],
        "album_name": track["album"]["name"],
        "artist_id": track["artists"][0]["id"],
        "artist_name": track["artists"][0]["name"],
        "played_at": item["played_at"]
    }

@mcp.tool()
def get_top_artists(limit: int = 10):
    """
    Gets top artists on Spotify.
    Allows Claude to answer "Who are my top 10 artists?"
    """
    spotify = get_spotify_client()
    results = spotify.current_user_top_artists(limit=limit)
    
    artists_parsed = [parse_artist(artist) for artist in results['items']]

    return artists_parsed

@mcp.tool()
def get_recently_played(limit: int = 10):
    """
    Gets recently played songs on Spotify.
    Allows Claude to answer "What songs have I listened to recently?"
    """
    spotify = get_spotify_client()
    results = spotify.current_user_recently_played(limit=limit)
    
    songs_parsed = [parse_recently_played(song) for song in results['items']]

    return songs_parsed


if __name__ == "__main__":
    mcp.run()