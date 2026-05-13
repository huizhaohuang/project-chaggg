"""Download cleaned parquet from Google Drive if not present locally."""
import os
import gdown

PARQUET_PATH = os.path.join("data", "cleaned", "chicago_crimes_cleaned.parquet")
GDRIVE_ID = "1bhVZEIXr8jjuNfIv9nWIyPQPvxPyd7ir"

def download():
    if os.path.exists(PARQUET_PATH):
        print(f"Data already exists at {PARQUET_PATH}, skipping download.")
        return
    os.makedirs(os.path.dirname(PARQUET_PATH), exist_ok=True)
    print(f"Downloading parquet from Google Drive...")
    gdown.download(id=GDRIVE_ID, output=PARQUET_PATH, quiet=False)
    print(f"Done! Saved to {PARQUET_PATH}")

if __name__ == "__main__":
    download()
