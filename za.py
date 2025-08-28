# app.py
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# ====================================
# ADD YOUR GOOGLE GEMINI API KEY HERE
# ====================================
genai.configure(api_key="AIzaSyDTxuq4Y7ClEipS478_nCtEMiZE1iimCjw")  # <-- Replace with your key

# Choose model
model = genai.GenerativeModel("gemini-1.5-flash")  # Can use gemini-pro or gemini-1.5-pro

@app.route("/")
def index():
    return render_template("index.html")  # Create HTML UI separately

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")

    try:
        # Call Gemini API
        response = model.generate_content(user_message)
        bot_reply = response.text.strip()
        return jsonify({"reply": bot_reply})

    except Exception as e:
        return jsonify({"error": str(e)})
    

    @app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    print(f"Received message: {user_message}")  # Debug

    try:
        response = model.generate_content(user_message)
        bot_reply = response.text.strip()
        print(f"Bot reply: {bot_reply}")  # Debug
        return jsonify({"reply": bot_reply})

    except Exception as e:
        print(f"Error: {e}")  # Debug
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
