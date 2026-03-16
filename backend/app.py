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

    try:
        data = request.json
        message = data.get("message")

        if not message:
            return jsonify({
                "reply": "Please enter a fitness question."
            })

        response = get_fitness_response(message)

        return jsonify({
            "reply": response
        })

    except Exception as e:
        return jsonify({
            "reply": "An error occurred while processing the request."
        })
