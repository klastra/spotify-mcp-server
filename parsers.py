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

def parse_listening_history(row) -> dict:
    return dict(row)


def parse_artist_play_count(row):
    return {
        "artist_name": row["artist_name"],
        "play_count": row["play_count"]
    }