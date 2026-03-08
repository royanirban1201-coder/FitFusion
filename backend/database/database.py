from motor.motor_asyncio import AsyncIOMotorClient
from app.config import MONGODB_URL, DATABASE_NAME

client = AsyncIOMotorClient(MONGODB_URL)

database = client[DATABASE_NAME]

user_collection = database.get_collection("users")

food_collection = database["food_logs"]

activity_collection = database["activities"]