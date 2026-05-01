# MongoDB Integration - Quick Start Guide

## ✅ What Has Been Done

1. **Updated `database/db.py`** - Added 3 functions for MongoDB operations:
   - `save_chat_to_mongodb()` - Saves user and bot messages with timestamp
   - `get_all_chats()` - Retrieves all conversations from MongoDB
   - `clear_all_chats()` - Deletes all chat history

2. **Updated `app.py`** - Modified chat routes to use MongoDB:
   - `/chat` route now saves conversations to MongoDB Atlas
   - `/history` route loads chats from MongoDB
   - `/clear_history` route clears MongoDB database

3. **Updated `requirements.txt`** - Added `pymongo` package

4. **Updated `templates/history.html`** - Enhanced UI to show timestamps

5. **Installed dependencies** - `pymongo` is now installed

## 🚀 Next Steps

### 1. Set Up MongoDB Atlas (5 minutes)

Follow the detailed guide in [MONGODB_SETUP.md](./MONGODB_SETUP.md):
- Create free MongoDB Atlas account
- Create a cluster
- Create database user
- Get connection string

### 2. Configure Environment Variables

In `new-chatbot-AI/database/.env`, add:

```env
MONGO_URL=mongodb+srv://YOUR_USERNAME:YOUR_PASSWORD@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority
MONGO_DB=chatbot_ai_db
```

Replace:
- `YOUR_USERNAME` - Your MongoDB Atlas username
- `YOUR_PASSWORD` - Your MongoDB Atlas password
- `cluster0.xxxxx` - Your actual cluster name

### 3. Test the Connection

```bash
cd new-chatbot-AI
python app.py
```

Visit `http://localhost:5000` and:
1. Send a test message
2. Look at console - should show: ✓ Chat saved to MongoDB with ID: ...
3. Click "Chat History" to see your messages stored in MongoDB

### 4. (Optional) Install MongoDB Compass

For local database visualization:
1. Download from: https://www.mongodb.com/products/compass
2. Use the same connection string
3. Browse collections in `chatbot_ai_db` → `chat_history`

## 📊 Your Data Flow

```
User Message
    ↓
Flask App (app.py)
    ↓
Groq LLM (medibot.py)
    ↓
Bot Response
    ↓
save_chat_to_mongodb() ──→ MongoDB Atlas (Cloud)
                        ↓
                    MongoDB Compass (Local - optional)
    ↓
Stored with Timestamp
    ↓
Retrieved by /history route
    ↓
Displayed in UI
```

## 📝 MongoDB Structure

Each chat entry stores:
```json
{
  "_id": "ObjectId",
  "user": "User's question",
  "bot": "Bot's answer",
  "timestamp": "2024-01-15T10:30:00.000Z"
}
```

## 🔍 Where to View Your Data

### MongoDB Atlas Dashboard:
1. Log in to MongoDB Atlas
2. Go to your cluster
3. Click "Collections"
4. Navigate to `chatbot_ai_db` → `chat_history`

### MongoDB Compass:
1. Open MongoDB Compass
2. Paste your connection string
3. Browse `chatbot_ai_db` → `chat_history`

### Your Flask App:
1. Visit `/history` page
2. See all conversations with timestamps

## 🛠️ Troubleshooting

| Issue | Solution |
|-------|----------|
| "MONGO_URL is not set" | Add `.env` file in `database/` folder with correct connection string |
| "Cannot connect to cluster" | Ensure IP is whitelisted in MongoDB Atlas Network Access |
| "Connection refused" | Check internet, verify credentials, restart app |
| No data showing in Atlas | Check if MongoDB is saving (look for ✓ in console logs) |

## 📚 Files Modified

- `database/db.py` - Added MongoDB functions
- `app.py` - Updated routes to use MongoDB
- `requirements.txt` - Added pymongo
- `templates/history.html` - Enhanced timestamp display

## ✨ Features

✅ Automatic cloud backup (MongoDB Atlas)  
✅ Timestamps on all conversations  
✅ View history with timestamps  
✅ Clear all chat history with one click  
✅ Local browsing with MongoDB Compass  
✅ Scalable cloud storage  
✅ No local JSON file needed  

## 🎯 Next: Test It Out!

1. Start your Flask app: `python app.py`
2. Send a message through the chatbot
3. Check the console for "✓ Chat saved to MongoDB"
4. Visit `/history` to see stored conversations
5. Log in to MongoDB Atlas and verify data is there!

Happy chatting! 🚀
