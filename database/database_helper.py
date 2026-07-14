import pyodbc
from parsers.parsers import parse_artist_play_count, parse_listening_history, rows_to_dicts
from config import (
    SQL_SERVER_DRIVER,
    SQL_SERVER_HOST,
    SQL_SERVER_PORT,
    SQL_SERVER_DATABASE,
    SQL_SERVER_USERNAME,
    SQL_SERVER_PASSWORD
)

def get_connection():
    connection_string = (
        f"DRIVER={{{SQL_SERVER_DRIVER}}};"
        f"SERVER={SQL_SERVER_HOST},{SQL_SERVER_PORT};"
        f"DATABASE={SQL_SERVER_DATABASE};"
        f"UID={SQL_SERVER_USERNAME};"
        f"PWD={SQL_SERVER_PASSWORD};"
        "TrustServerCertificate=yes;"
    )

    return pyodbc.connect(connection_string)

def insert_listening_history(track: dict) -> None:
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
        SELECT TOP (?)
            *
        FROM ListeningHistory;
        """,
        (limit,)
    )

    rows = cursor.fetchall()
    rows = rows_to_dicts(cursor, rows)

    conn.close()

    return [parse_listening_history(row) for row in rows]


def query_most_listened_artists(limit: int) -> list[dict]:
    conn = get_connection()

    cursor = conn.execute(
    """
    SELECT TOP (?)
        artist_name,
        COUNT(*) AS play_count
    FROM ListeningHistory
    GROUP BY artist_name
    ORDER BY play_count DESC;
    """,
    (limit,)
    )

    rows = cursor.fetchall()
    rows = rows_to_dicts(cursor, rows)

    conn.close()

    return [parse_artist_play_count(row) for row in rows]


def listening_event_exists(track_id, played_at) -> bool:
    conn = get_connection()

    cursor = conn.execute(  
        """
        SELECT TOP 1 1 FROM ListeningHistory
        WHERE track_id = ?
        AND played_at = ?
        """,
        (track_id, played_at)
    )

    track_exists = cursor.fetchone() is not None

    conn.close()

    return track_exists