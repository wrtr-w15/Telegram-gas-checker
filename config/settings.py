# config/settings.py
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
RPC_URL = os.getenv("RPC_URL")
ALERT_THRESHOLD = int(os.getenv("ALERT_THRESHOLD", 20))
CHECK_INTERVAL = int(os.getenv("CHECK_INTERVAL", 60))