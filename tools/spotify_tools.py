from mcp_server import mcp
from services import spotify_service
from config import DEFAULT_LIMIT

@mcp.tool()
def fetch_top_artists_from_spotify(limit: int = DEFAULT_LIMIT) -> list[dict]:
    """
    Gets top artists on Spotify.
    Allows Claude to answer "Who are my top 10 artists?"
    """
    return spotify_service.fetch_top_artists_from_spotify(limit)

@mcp.tool()
def fetch_recently_played_from_spotify(limit: int = DEFAULT_LIMIT) -> list[dict]:
    """
    Gets recently played songs on Spotify.
    Allows Claude to answer "What songs have I listened to recently?"
    """
    return spotify_service.fetch_recently_played_from_spotify(limit)

@mcp.tool()
def sync_recently_played() -> dict:
    """
    Syncs recently played songs into the database.
    Checks if song being inserted already exists in the database before inserting.
    Returns a dict of status and message, including count of new songs listened to
    """
    return spotify_service.sync_recently_played()