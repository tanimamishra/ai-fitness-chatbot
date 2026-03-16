from flask import Flask, request, jsonify
from flask_cors import CORS
from fitness_logic import get_fitness_response

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "AI Fitness Chatbot Backend Running"


@app.route("/chat", methods=["POST"])
def chat():

    data = request.json
    message = data.get("message")

    response = get_fitness_response(message)

    return jsonify({
        "reply": response
    })
