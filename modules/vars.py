from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = "27952989"
API_HASH = "74f04808a359e9a516e955ec243613ca"
BOT_TOKEN = "6866810487:AAHkaTYQRKxMR-STBMlpwIiCm5bh1DfhBKQ"
OWNER_ID = "7146854725"
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7146854725").split()))
