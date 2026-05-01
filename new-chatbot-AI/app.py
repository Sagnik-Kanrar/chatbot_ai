from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_cors import CORS
from medibot import get_response
from dotenv import load_dotenv
from database.db import save_chat_to_mongodb, get_all_chats, clear_all_chats

import json
import os


app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    import traceback
    try:
        data = request.get_json(force=True)

        user_msg = data.get("message", "")

        print("Request Received")

        reply = get_response(user_msg)

        print("Reply ready")

        if not reply:
            reply = "Empty response from backend"

        # ✅ SAVE CHAT TO MONGODB
        try:
            save_chat_to_mongodb(user_msg, reply)
        except Exception as db_error:
            print(f"Warning: Failed to save to MongoDB: {db_error}")
            # Continue even if MongoDB save fails

        return jsonify({
            "response": str(reply)
        })

    except Exception as e:
        error = traceback.format_exc()
        print(error)

        return jsonify({
            "response": "Backend error",
            "error": error
        })


@app.route("/history")
def history():
    # ✅ Load history from MongoDB
    try:
        data = get_all_chats()
    except Exception as e:
        print(f"Error retrieving history from MongoDB: {e}")
        data = []

    return render_template("history.html", chats=data)




@app.route("/clear_history")
def clear_history():
    try:
        clear_all_chats()
    except Exception as e:
        print(f"Error clearing history: {e}")
        return str(e)

    # ✅ redirect back to history so the cleared state is visible immediately
    return redirect(url_for("history"))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)