## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "1ApWapzMBuwPp14lii-95UMVmOYgyU8xwXtZrnJwGGaEJgaRqpCMbACPyVfOhJITzHcDSOO0hY-nI1KsbYniW_6GrEunC7B2VXcnQgHIa7DnCw7156ZnEeQrvGhMNRydXMVxxE23yKcyQu4oyE6v0s3mGGkhgIFXEPaVgo7dX200MmO2FrV_Ke-8a4FPwFLxwGgxpYNGqyz6efOEj206JEnOCUiw2s0qDhMBzfxPsYUEv9rUbWoCFwNwUs8VCOEnyZfyJlxwA1zevQ_bFAlVOELXgEJvWO_KNGYivFfLF8xzg3Go1yaLF_F1AJ-Ak8-x_2w8kAlR5cKS66aOZLbZXiRhoVQAKBcQ=")
BOT_TOKEN = getenv("BOT_TOKEN", "5390015866:AAHEmkVI_aUdVZTL3tQ37gXuisxuMYmuDrE")
BOT_NAME = getenv("BOT_NAME", "music")
API_ID = int(getenv("API_ID", "19802523"))
API_HASH = getenv("API_HASH", "6bd1987bc3591e2db53b4edc5b4867b5")
OWNER_NAME = getenv("OWNER_NAME", "𝐌𝐔𝐒𝐈𝐂࿚")
OWNER_USERNAME = getenv("OWNER_USERNAME", "@t_4lb")
ALIVE_NAME = getenv("ALIVE_NAME", "هـوس")
BOT_USERNAME = getenv("BOT_USERNAME", "t_4lo_bot")
OWNER_ID = getenv("OWNER_ID", "1777087402")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "il_li0ll")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "tabarkalaa123")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "tabarkalaa123")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5383415297").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/46fa55b49b85c084159ce.png")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/466de30ee0f9383c8e09e.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/46fa55b49b85c084159ce.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/a282c460a7f98aedbe956.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/8fe190a2a52986bd29dc5.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
