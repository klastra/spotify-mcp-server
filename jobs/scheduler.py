import time
from jobs.sync_job import run
from config import SYNC_INTERVAL_SECONDS

def main():
    """
    Calls sync_job's run() every 30 minutes.
    """
    print("Spotify scheduler started...")

    while True:
        try:
            run()
        except Exception as ex:
            print(f"Sync failed: {ex}")
        
        print(f"Sleeping for {SYNC_INTERVAL_SECONDS} seconds...\n")
        time.sleep(SYNC_INTERVAL_SECONDS)

if __name__ == "__main__":
    main()