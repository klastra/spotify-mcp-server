from mcp_server import mcp
from database.database_helper import query_listening_history, query_listening_summary, query_most_listened_artists
from config import DEFAULT_LIMIT

@mcp.tool()
def get_listening_history(limit: int = DEFAULT_LIMIT) -> list[dict]:
    """
    Gets listening history from the local database.
    This is used for analyzing listening patterns.
    """
    return query_listening_history(limit)

@mcp.tool()
def get_most_played_artists(limit: int = DEFAULT_LIMIT) -> list[dict]:
    """
    Gets most played artists based on history.
    Answers "Among the listening events I've collected, who appears most often?"
    """
    return query_most_listened_artists(limit)

@mcp.tool()
def get_listening_summary() -> dict:
    """
        Provides a summary of listening activity collected in the database.
    Includes total (track) plays, unique artists, and unique tracks.
    """
    return query_listening_summary()