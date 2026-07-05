from pyrogram import Client, filters
from database import movies

pending = {}

@Client.on_message(filters.command("addmovie"))
async def addmovie(client, message):
    pending[message.from_user.id] = {}
    await message.reply_text(
        "Send:\nTitle|Year\n\nExample:\nAvatar|2009"
    )

@Client.on_message(filters.text)
async def get_title(client, message):
    user = message.from_user.id

    if user not in pending:
        return

    if "title" not in pending[user]:
        try:
            title, year = message.text.split("|")
        except:
            return

        pending[user]["title"] = title.strip()
        pending[user]["year"] = year.strip()

        await message.reply_text(
            "Now send the movie video."
        )

@Client.on_message(filters.video)
async def save_video(client, message):
    user = message.from_user.id

    if user not in pending:
        return

    title = pending[user]["title"]
    year = pending[user]["year"]

    await movies.insert_one({
        "title": title.lower(),
        "year": year,
        "file_id": message.video.file_id
    })

    del pending[user]

    await message.reply_text(
        "✅ Movie Saved Successfully"
    )
