from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "AI Fitness Chatbot Backend Running"


@app.route("/chat", methods=["POST"])
def chat():

    data = request.json
    message = data.get("message")

    return jsonify({
        "reply": "Backend received message: " + message
    })
