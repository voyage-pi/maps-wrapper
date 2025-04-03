import os
from dotenv import load_dotenv
from pathlib import Path

# Get the base directory of your project
BASE_DIR = Path(__file__).resolve().parent.parent
print(f"Looking for .env file in: {os.path.join(BASE_DIR, '.env')}")

# Load environment variables from .env file with explicit path
load_dotenv(os.path.join(BASE_DIR, '.env'))

GOOGLE_MAPS_API_KEY = os.getenv("GOOGLEMAPSAPIKEY")
print(f"GOOGLE_MAPS_API_KEY value: {GOOGLE_MAPS_API_KEY}")

if not GOOGLE_MAPS_API_KEY:
    raise ValueError("GOOGLE_MAPS_API_KEY is missing or not loaded correctly")
