from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import smtplib
from email.message import EmailMessage
import requests
import config

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, methods=["GET", "POST", "OPTIONS"])

# MongoDB setup
client = MongoClient(config.MONGO_URI)
db = client.get_database("contactform")
collection = db.get_collection("submissions")

@app.route("/send-email", methods=["POST"])
def send_email():
    try:
        data = request.json
        name = data.get("name")
        email = data.get("email")
        message = data.get("message")

        # Save to MongoDB
        collection.insert_one({
            "name": name,
            "email": email,
            "message": message
        })

        # Send email via Gmail
        msg = EmailMessage()
        msg['Subject'] = f"New Contact Form Submission from {name}"
        msg['From'] = config.EMAIL_USER
        msg['To'] = config.EMAIL_USER
        msg.set_content(f"Name: {name}\nEmail: {email}\n\n{message}")

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(config.EMAIL_USER, config.EMAIL_PASS)
            smtp.send_message(msg)

        return jsonify({"status": "success", "message": "Email sent and stored!"})
    except Exception as e:
        print("Error:", e)
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    prompt = data.get("prompt", "")

    if not prompt:
        return jsonify({"response": "⚠️ Prompt is empty."}), 400

    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
    "Authorization": f"Bearer {config.OPENROUTER_API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "https://fastfullstack.netlify.app",  # required by OpenRouter
    "X-Title": "SmartWriter"
}

    payload = {
    "model": "openai/gpt-3.5-turbo",
    "messages": [
        {
            "role": "user",
            "content": prompt
        }
    ]
}


    try:
        res = requests.post(url, headers=headers, json=payload)
        res.raise_for_status()
        response_text = res.json()['choices'][0]['message']['content']
        return jsonify({"response": response_text})
    except Exception as e:
        print("OpenRouter error:", e)
        return jsonify({"response": "⚠️ OpenRouter response failed."}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8000)
