import os
from motor.motor_asyncio import AsyncIOMotorClient
from passlib.context import CryptContext
from dotenv import load_dotenv
import asyncio

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")
DB_NAME = os.getenv("DB_NAME")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

if not MONGO_URL or not DB_NAME:
    raise ValueError("❌ Missing MONGO_URL or DB_NAME in .env file")

client = AsyncIOMotorClient(MONGO_URL)
db = client[DB_NAME]

async def reset_and_create_admin():
    users_col = db["users"]

    result = await users_col.delete_many({})
    print(f"✅ Deleted {result.deleted_count} users from 'users' collection.")

    admin_user = {
        "email": "admin@example.com",
        "hashed_password": pwd_context.hash("admin123"[:72]), # Truncate for bcrypt compatibility
        "is_admin": True
    }
    
    await users_col.insert_one(admin_user)
    print("✅ Admin user created successfully.")

if __name__ == "__main__":
    asyncio.run(reset_and_create_admin())