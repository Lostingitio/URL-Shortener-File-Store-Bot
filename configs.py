# (c) @PredatorHackerzZ || @TeleRoidGroup

import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "4682685"))
  PORT = os.environ.get("PORT","8080")
  API_HASH = os.environ.get("API_HASH", "3eba5d471162181b8a3f7f5c0a23c307")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "6268614122:AAFR6tNKLlO86cr5erLjQsDnWHlLHNakQo4")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "shazam_TB_bot")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1001868547833"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "PaisaKamalo.in")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "9d7e32c571c44b3ee91a814fa25c31e0211f5aeb")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "945284066"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://misoc51233:filestore@cluster0.imfn5pn.mongodb.net/?retryWrites=true&w=majority")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "movie_time_botonly")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001634620304"))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ 🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅]────⍟
│
├🔸 My Name: [FileStore Bot](https://t.me/{BOT_USERNAME})
│
├🔸 Language: [Python 3](https://www.python.org)
│
├🔹 Library: [Pyrogram](https://docs.pyrogram.org)
│
╰──────[ 😎 ]───────────⍟
"""
  ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: [Me](https://t.me/fligher)
 
 I am Super noob Please Support My Hard Work.


"""
  HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent FileStore Bot.

Join: @movie_time_botonly"""
