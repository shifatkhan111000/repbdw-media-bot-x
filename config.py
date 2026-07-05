import os
from dotenv import load_dotenv

load_dotenv()

# Telegram
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# MongoDB
MONGO_URI = os.getenv("MONGO_URI")

# Admin
ADMIN_ID = int(os.getenv("ADMIN_ID"))

# Bot Info
BOT_NAME = "RepBDW Media Bot X"
VERSION = "2.0.0"
