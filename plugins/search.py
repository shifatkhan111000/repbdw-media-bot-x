from pyrogram import Client, filters

@Client.on_message(filters.command("search"))
async def search_movie(client, message):
    if len(message.command) < 2:
        return await message.reply_text(
            "Usage: /search movie_name"
        )

    movie = " ".join(message.command[1:])
    await message.reply_text(
        f"Searching for: {movie}"
    )
