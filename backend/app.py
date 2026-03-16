from flask import Flask, request, jsonify
from flask_cors import CORS
from fitness_logic import get_fitness_response

app = Flask(__name__)
CORS(app)

@app.route("/chat", methods=["POST"])
def chat():

    data = request.json
    user_message = data.get("message")

    response = get_fitness_response(user_message)

    return jsonify({
        "reply": response
    })


if __name__ == "__main__":
    app.run()
