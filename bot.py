from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN

app = Client(
    "RepBDWMediaBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message()
async def alive(client, message):
    if message.text == "/start":
        await message.reply_text(
            "🔥 RepBDW Media Bot X\n\n"
            "✅ Bot is Online!"
        )

print("🚀 Starting RepBDW Media Bot X...")
app.run()
