import sqlite3

from parsers import parse_artist_play_count, parse_listening_history

def get_connection():
    conn = sqlite3.connect("spotify.db")
    conn.row_factory = sqlite3.Row
    return conn

def initialize_database():
    conn = get_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS ListeningHistory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            track_id TEXT,
            track_name TEXT,
            album_name TEXT,
            artist_id TEXT,
            artist_name TEXT,
            played_at TEXT
                 
            UNIQUE (track_id, played_at)
        );
    """)

    conn.commit()
    conn.close()


def insert_listening_history(track):
    conn = get_connection()

    conn.execute(
        """
        INSERT INTO ListeningHistory (
            track_id,
            track_name,
            album_name,
            artist_id,
            artist_name,
            played_at
        )
        VALUES
        (
            ?, ?, ?, ?, ?, ?
        )
        """,
        (
            track["track_id"],
            track["track_name"],
            track["album_name"],
            track["artist_id"],
            track["artist_name"],
            track["played_at"]
        )
    )

    conn.commit()
    conn.close()

def query_listening_history(limit: int) -> list[dict]:
    conn = get_connection()

    cursor = conn.execute(
        """
        SELECT * FROM ListeningHistory
        LIMIT ?
        """,
        (limit, )
    )

    rows = cursor.fetchall()

    conn.close()

    return [parse_listening_history(row) for row in rows]


def query_most_listened_artists(limit: int):
    conn = get_connection()

    cursor = conn.execute(
        """
        SELECT
            artist_name,
            COUNT(*) AS play_count
        FROM ListeningHistory
        GROUP BY artist_name
        ORDER BY play_count DESC
        LIMIT ?;
        """,
        (limit,)
    )

    rows = cursor.fetchall()

    conn.close()

    return [parse_artist_play_count(row) for row in rows]


def listening_event_exists(track_id, played_at) -> bool:
    conn = get_connection()

    cursor = conn.execute(  
        """
        SELECT 1 FROM ListeningHistory
        WHERE track_id = ?
        AND played_at = ?
        LIMIT 1 
        """,
        (track_id, played_at)
    )

    track_exists = cursor.fetchone() is not None

    conn.close()

    return track_exists