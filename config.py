import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "5351355388,6616561731")) #optional
API_HASH = getenv("API_HASH", "16e57cb1d4c5f250cb5f3a28646f0e4b") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6371879956").split()))
OWNER_ID = int(getenv("OWNER_ID", "6371879956"))
MONGO_URL = getenv("MONGO_URL", "mongodb://localhost:27017")
BOT_TOKEN = getenv("BOT_TOKEN", "8114099090:AAEvjgQ-ymC7SauA3FvtsJ4dJZ0DszBOq_w")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://telegra.ph/file/3c52a01057865f7511168.jpg')
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP", "@fxyycxx")
GIT_TOKEN = getenv("GIT_TOKEN", "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") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/fxyy2009/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
