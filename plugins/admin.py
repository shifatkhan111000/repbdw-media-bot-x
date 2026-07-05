from pyrogram import Client, filters
from config import ADMINS

@Client.on_message(filters.command("admin"))
async def admin_panel(client, message):
    if message.from_user.id not in ADMINS:
        return

    await message.reply_text("Admin Panel")
