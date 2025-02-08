from flask import Flask, jsonify
from flask_cors import CORS
from db import init_db
from auth import auth_bp

app = Flask(__name__)
CORS(app)  # Enables CORS for all routes

init_db()


app.register_blueprint(auth_bp, url_prefix="/auth")


@app.route("/")
def home():
    return jsonify({"message": "Welcome to my simple Python backend!"})


@app.route("/api/data")
def get_data():
    return jsonify({"data": ["Item 1", "Item 2", "Item 3"]})


if __name__ == "__main__":
    app.run(debug=True)
