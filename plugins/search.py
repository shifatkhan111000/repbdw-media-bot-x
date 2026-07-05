from pyrogram import Client, filters
from database import movies

@Client.on_message(filters.text)
async def search_movie(client, message):

    movie = await movies.find_one({
        "title": message.text.lower()
    })

    if not movie:
        return

    await message.reply_text(
        f"🎬 {movie['title'].title()} ({movie['year']})"
    )

    await client.send_video(
        chat_id=message.chat.id,
        video=movie["file_id"]
    )
