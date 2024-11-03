import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
admins = {}
SESSION_NAME = getenv("BQHFmUgAwzDySLMT945VnCI5m4fJ5DB2-sAkRvg29RnLJNlEdTFbIEMj-ESSCHLRhhFxdPyxrjg2InxIWALUvKm290fPmSQ9Z2T73QxgLcoa_2BQy1mgzkX5kSPNNFtg5ybRFXC5Ya07TXSGYRqlhFzPL_hzZ3WSh44RO7iM-6ZoXoO5XXQz2ngUjAl0ipt64ywZDHOUQI3kR7Frk2lAfk-KAMLJS9ggog4efXDyIRvOHe_0ImDmWWKPTE_4RQOl3736lQRzG0aiv4bIPuF3a8Vi0xeqN8oIMBFJQfzbevVvmqmgNuRyXKO1QK3aKnF_NXGtyYjupXqHKX9L0TrFIC-AW3repgAAAAGd2xVtAA", "session")
BOT_TOKEN = getenv("7605039383:AAE1mgOumbsRbJo6OYP2GUxTOCmZS68-qYs")
BOT_NAME = getenv("BOT_NAME", "𝙓44 𝙈𝙪𝙨𝙞𝙘 𝙑𝙖𝙪𝙡𝙩")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/6790864f5fe27471bdc8d.png")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/e9a4d6655e5ddf51f9160.jpg")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/91034f175d41040d45b38.jpg")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/c8a0e9c544c5ea689caf9.jpg")
API_ID = int(getenv("29727048"))
API_HASH = getenv("38d104adbd94c66a349714abd7977d80")
BOT_USERNAME = getenv("BOT_USERNAME", "X44MusicVaultRobot)
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "X44MusicVault")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "+zdzQ87N-ntxiZDNl)
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "+565zq0XLr2g1ZjI1)
OWNER_NAME = getenv("OWNER_NAME", "會 | ɪ ꪖꪑ • SHAHIL") # isi dengan username kamu tanpa simbol @
PMPERMIT = getenv("PMPERMIT", None)
OWNER_ID = int(os.environ.get("6943348077")) # fill with your id as the owner of the bot
DATABASE_URL = os.environ.get("mongodb+srv://ms7371091:ms7371091@cluster0.vwfw6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # fill with your mongodb url
LOG_CHANNEL = int(os.environ.get("-1002467044807")) # make a private channel and get the channel id
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False)) # just fill with True or False (optional)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
LANG = getenv("LANG", "id")
