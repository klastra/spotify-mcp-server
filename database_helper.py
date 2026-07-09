import sqlite3

from main import parse_listening_history

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

def query_from_listening_history() -> list[tuple[str, str]]:
    conn = get_connection()

    cursor = conn.execute(
        """
        SELECT * FROM ListeningHistory
        """
    )

    rows = cursor.fetchall()

    conn.close()

    return [parse_listening_history(row) for row in rows]