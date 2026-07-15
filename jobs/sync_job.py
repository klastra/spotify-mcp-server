from services.spotify_service import sync_recently_played

def run():
    print("Starting Spotify listening activity synchronization...")
    result = sync_recently_played()
    print(result["message"])

if __name__ == "__main__":
    run()