## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "1ApWapzMBuyCqidQO8gXb8o3DLjb3jVCWLas6NRRCND5TwU0DCMHPDXUW0Q5tMFwME1AFsW5b3MRmsN3TQscHR81hz95U6-uzqXCI20jzMjT3XjzMmTCxaMN--Dn28yTfgQYQAc-491V7OvVZETLOIEmOZSGf0biJrwUD0cO27MAr7NaknTqUgKCZXCbEmpu0DSEeq3ruBjiprfcy4EcjvmMmkhqQCQA0_RhgDEXhU20WTy6PYnLQp4phSPVjxyuyBv83AqUs9Uawu33FYh9-GnGEJ9UJRbzg7bfb8y0IqvVlYjbilWiPcQCQG-Lb3d0KEo2KtwyTJAWJL9kbNY5bYjxrMzdARUo=")
BOT_TOKEN = getenv("BOT_TOKEN", "5493176924:AAGQLteUpNSwFKuLxt7hqg5q4U8GZjCn6U4")
BOT_NAME = getenv("BOT_NAME", "جنازه")
API_ID = int(getenv("API_ID", "9886198"))
API_HASH = getenv("API_HASH", "8b8ad1d2c4e0e590f827478d7989cfe2")
OWNER_NAME = getenv("OWNER_NAME", "Julia")
OWNER_USERNAME = getenv("OWNER_USERNAME", "FGADIENBOT")
ALIVE_NAME = getenv("ALIVE_NAME", "S_jj_j")
BOT_USERNAME = getenv("BOT_USERNAME", "")
OWNER_ID = getenv("OWNER_ID", "5279880364")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5284259786").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/e22e5d1f0ccd57fa5f677.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
