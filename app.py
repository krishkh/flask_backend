from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enables CORS for all routes


@app.route("/")
def home():
    return jsonify({"message": "Welcome to my simple Python backend!"})


@app.route("/api/data")
def get_data():
    return jsonify({"data": ["Item 1", "Item 2", "Item 3"]})


if __name__ == "__main__":
    app.run(debug=True)
