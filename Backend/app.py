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
    try:
        data = request.get_json(silent=True) or {}
        prompt = (data.get("prompt") or "").strip()
        if not prompt:
            return jsonify({"response": "⚠️ Prompt is empty."}), 400

        url = "https://openrouter.ai/api/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {config.OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
            "X-Title": "SmartWriter",
            # "Referer": "https://fastfullstack.netlify.app",  # optional; if you include it, use this exact key
        }
        payload = {
            "model": "openai/gpt-4o-mini",
            "messages": [
                {"role": "system", "content": "You are a helpful writing assistant."},
                {"role": "user", "content": prompt},
            ],
        }

        res = requests.post(url, headers=headers, json=payload, timeout=30)
        if not res.ok:
            try:
                print("OpenRouter error:", res.status_code, res.json())
            except Exception:
                print("OpenRouter error:", res.status_code, res.text)
            code = res.status_code
            if code == 401:
                msg = "Invalid/missing API key."
            elif code == 402:
                msg = "Insufficient credits for the selected model."
            elif code == 404:
                msg = "Model unavailable—try a different one."
            elif code == 429:
                msg = "Rate limited—please retry shortly."
            else:
                msg = f"Upstream error ({code})."
            return jsonify({"response": f"⚠️ {msg}"}), 502

        j = res.json()
        content = (j.get("choices", [{}])[0].get("message", {}) or {}).get("content")
        if not content:
            print("Unexpected OpenRouter response:", j)
            return jsonify({"response": "⚠️ Unexpected response format from model."}), 502

        return jsonify({"response": content})
    except requests.Timeout:
        return jsonify({"response": "⚠️ Model request timed out. Try again."}), 504
    except Exception as e:
        print("Generate() exception:", repr(e))
        return jsonify({"response": "⚠️ Server error while generating text."}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8000)
