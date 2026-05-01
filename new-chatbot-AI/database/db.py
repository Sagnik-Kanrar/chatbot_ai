import os
from pathlib import Path
from dotenv import load_dotenv
from pymongo import MongoClient
from gridfs import GridFS
from datetime import datetime

env_path = Path(__file__).resolve().parent / ".env"
if env_path.exists():
    load_dotenv(dotenv_path=env_path)
else:
    load_dotenv()

mongo_url = os.getenv("MONGO_URL")
if not mongo_url:
    raise RuntimeError("MONGO_URL is not set in database/.env or environment variables")

client = MongoClient(mongo_url)
MONGO_DB = os.getenv("MONGO_DB", "chatbot_ai_db")  # Default to 'chatbot_ai_db' if not set
db = client[MONGO_DB]

# Initialize GridFS for storing files
# This creates fs.files and fs.chunks collections automatically
fs = GridFS(db)

# Collection for storing chat history
chat_collection = db["chat_history"]


def save_chat_to_mongodb(user_message, bot_response):
    """
    Save chat conversation to MongoDB
    
    Args:
        user_message (str): The user's message
        bot_response (str): The bot's response
        
    Returns:
        str: The ID of the inserted document
    """
    try:
        chat_document = {
            "user": user_message,
            "bot": bot_response,
            "timestamp": datetime.utcnow()
        }
        result = chat_collection.insert_one(chat_document)
        print(f"✓ Chat saved to MongoDB with ID: {result.inserted_id}")
        return str(result.inserted_id)
    except Exception as e:
        print(f"✗ Error saving chat to MongoDB: {e}")
        raise


def get_all_chats():
    """
    Retrieve all chat history from MongoDB
    
    Returns:
        list: List of chat documents sorted by timestamp (newest first)
    """
    try:
        chats = list(chat_collection.find({}).sort("timestamp", -1))
        # Convert ObjectId to string and format timestamp for JSON serialization
        for chat in chats:
            chat["_id"] = str(chat["_id"])
            # Format timestamp as readable string
            if "timestamp" in chat:
                timestamp = chat["timestamp"]
                chat["timestamp"] = timestamp.strftime("%B %d, %Y at %I:%M %p")
        return chats
    except Exception as e:
        print(f"✗ Error retrieving chats from MongoDB: {e}")
        return []


def clear_all_chats():
    """
    Delete all chat history from MongoDB
    
    Returns:
        int: Number of documents deleted
    """
    try:
        result = chat_collection.delete_many({})
        print(f"✓ Cleared {result.deleted_count} chats from MongoDB")
        return result.deleted_count
    except Exception as e:
        print(f"✗ Error clearing chats from MongoDB: {e}")
        raise
