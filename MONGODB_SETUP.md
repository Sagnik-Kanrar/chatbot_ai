# MongoDB Setup Guide for Chatbot

This guide will help you set up MongoDB Atlas and connect your chatbot to store conversations.

## Step 1: Create a MongoDB Atlas Account

1. Go to [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
2. Sign up for a free account
3. Verify your email

## Step 2: Create a Cluster

1. Click "Create" to create a new project
2. Click "Build a Cluster"
3. Select **M0 (Free)** for testing
4. Choose your preferred region
5. Click "Create Cluster" (this takes 1-3 minutes)

## Step 3: Create Database User

1. In the left sidebar, click **Database Access**
2. Click **Add New Database User**
3. Enter:
   - Username: `chatbot_user` (or your choice)
   - Password: Create a strong password
   - Choose **Built-in Role**: `readWriteAnyDatabase`
4. Click **Add User**

## Step 4: Configure IP Whitelist

1. In the left sidebar, click **Network Access**
2. Click **Add IP Address**
3. Select **Allow Access from Anywhere** (for development)
   - Click the IP address field
   - Click "Allow Access from Anywhere"
4. Click **Confirm**

## Step 5: Get Connection String

1. Click the **Connect** button on your cluster
2. Select **Drivers**
3. Select **Python** version **3.6+**
4. Copy the connection string (it looks like):
   ```
   mongodb+srv://<username>:<password>@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority
   ```

## Step 6: Update Environment Variables

### Option A: Using .env file in the database folder

Create or update `.env` file in `new-chatbot-AI/database/.env`:

```env
MONGO_URL=mongodb+srv://chatbot_user:YOUR_PASSWORD@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority
MONGO_DB=chatbot_ai_db
```

Replace:
- `chatbot_user` with your database username
- `YOUR_PASSWORD` with your database password
- `cluster0.xxxxx` with your actual cluster URL

### Option B: Using system environment variables (Recommended)

On Windows PowerShell:
```powershell
$env:MONGO_URL="mongodb+srv://chatbot_user:YOUR_PASSWORD@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority"
$env:MONGO_DB="chatbot_ai_db"
```

## Step 7: Install MongoDB Compass (Optional - for local viewing)

1. Download [MongoDB Compass](https://www.mongodb.com/products/compass)
2. Install it
3. Use the same connection string to connect locally
4. You'll see `chatbot_ai_db` → `chat_history` collection with all your conversations

## Step 8: Test the Connection

Run your Flask app:
```bash
python app.py
```

Send a test message through the chatbot UI. You should see:
- ✓ Chat saved to MongoDB with ID: ... (in console)
- The message appears in MongoDB Atlas under: `chatbot_ai_db` → `chat_history`
- The message is visible in MongoDB Compass (if installed and connected)

## MongoDB Collection Structure

Your chat history is stored in this format:

```json
{
  "_id": ObjectId("..."),
  "user": "What is fever?",
  "bot": "Fever is an elevated body temperature...",
  "timestamp": ISODate("2024-01-15T10:30:00.000Z")
}
```

## Viewing Your Data

### In MongoDB Atlas Dashboard:
1. Go to your cluster
2. Click **Collections**
3. Select `chatbot_ai_db` → `chat_history`
4. Browse all conversations with timestamps

### In MongoDB Compass:
1. Open MongoDB Compass
2. Use your connection string
3. Navigate to `chatbot_ai_db` → `chat_history`
4. View and query conversations

## Troubleshooting

### Error: "MONGO_URL is not set"
- Make sure `.env` file exists in `new-chatbot-AI/database/`
- Or set system environment variables
- Restart your Flask app after setting variables

### Error: "Connection refused"
- Check your internet connection
- Verify IP address is whitelisted in MongoDB Atlas
- Confirm username and password are correct

### Error: "Cannot connect to cluster"
- Ensure cluster is running (green status in Atlas)
- Check connection string is correct
- Verify password doesn't have special characters (or URL encode them)

## Usage

Your chatbot automatically:
- ✓ Saves every conversation to MongoDB Atlas
- ✓ Stores with timestamp
- ✓ Displays in history page
- ✓ Can be viewed in MongoDB Compass
- ✓ Can be accessed via MongoDB Atlas dashboard
