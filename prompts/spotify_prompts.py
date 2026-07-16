from mcp_server import mcp

@mcp.prompt()
def spotify_wrapped():
    """
    Generate a Spotify Wrapped-style analysis.
    """
    return """
        Analyze my Spotify listening history and create a personalized Spotify Wrapped.

        Include:
        - Most played artists
        - Most played songs
        - Favorite albums
        - Listening patterns
        - Changes in music taste
        - Interesting observations
        - Surprising discoveries
    """


@mcp.prompt()
def discover_new_music():
    """
    Generate new music recommendations based on my music taste. 
    """
    return """
        Recommend new music based on my listening history.

        Include:
        - Artists similar to my favorites
        - Songs I might enjoy
        - Why each recommendation fits my taste
        - Artists I have not listened to yet
    """


@mcp.prompt()
def daily_listening_summary():
    """
    Generate a summary of listening habits for the current day.
    """
    return """
        Summarize my listening today.

        Include:
        - Number of songs played
        - Artists listened to
        - Most played artist
        - Listening timeline
        - Any interesting patterns
    """