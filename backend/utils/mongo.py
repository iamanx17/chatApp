from motor.motor_asyncio import AsyncIOMotorClient
mongo_url = 'mongodb+srv://iamanx17:2ceinwar@urlshortner.f1d74.mongodb.net'

client = AsyncIOMotorClient(mongo_url)

db = client['chatApp']
