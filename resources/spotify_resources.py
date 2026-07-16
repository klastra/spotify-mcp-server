from mcp_server import mcp
from database.database_helper import query_listening_history, query_most_listened_artists, query_listening_summary


@mcp.resource("spotify://history")
def listening_history_resource():
    """
    Provides access to stored Spotify listening history.
    """
    return query_listening_history(limit=50)


@mcp.resource("spotify://artists/top")
def top_artists_resource():
    """
    Provides access to the user's most played artists based on stored listening history.
    """
    return query_most_listened_artists(limit=20)


@mcp.resource("spotify://stats")
def listening_summary_resource():
    """
    Provides access to stored Spotify listening statisticts, 
    such as total plays, total unique artists listened to, 
    and unique tracks played.    
    """
    return query_listening_summary()