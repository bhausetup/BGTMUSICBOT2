from pyrogram import idle
from pyrogram import Client as Bot
from modules.clientbot import run
from modules.config import API_ID, API_HASH, BOT_TOKEN

    
bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="plugins")
)

bot.start()
run()
print("🥀 𝗔𝗻𝘀𝗵 𝗺𝘂𝘀𝗶𝗰 𝑩𝒐𝒕 𝑺𝒕𝒂𝒓𝒕𝒆𝒅 ✨ ...")
idle()
