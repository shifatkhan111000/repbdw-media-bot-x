from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient("YOUR_MONGODB_URI")

db = client.repbdw
movies = db.movies
