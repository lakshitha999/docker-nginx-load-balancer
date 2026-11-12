import socket

from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)

# Database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
    "DATABASE_URL",
    "postgresql+psycopg://appuser:apppassword@db:5432/userdb"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
with app.app_context():
    db.create_all()

# Allow React frontend to communicate with Flask
CORS(app, origins=["http://localhost:5173", "http://localhost:8080"])


# User database model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)


# Health check API
@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({
        "message": "Backend is working!",
        "container": socket.gethostname(),
        "version": "2.0"
    })

# Registration API
@app.route("/api/register", methods=["POST"])
def register():
    data = request.get_json() or {}

    name = data.get("name", "").strip()
    email = data.get("email", "").strip().lower()
    password = data.get("password", "")

    if not name or not email or not password:
        return jsonify({"error": "All fields are required"}), 400

    if len(password) < 6:
        return jsonify({"error": "Password must contain at least 6 characters"}), 400

    existing_user = User.query.filter_by(email=email).first()

    if existing_user:
        return jsonify({"error": "Email already registered"}), 409

    hashed_password = generate_password_hash(password)

    new_user = User(
        name=name,
        email=email,
        password=hashed_password
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "Registration successful!"}), 201


# Login API
@app.route("/api/login", methods=["POST"])
def login():
    data = request.get_json() or {}

    email = data.get("email", "").strip().lower()
    password = data.get("password", "")

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        return jsonify({"error": "Invalid email or password"}), 401

    return jsonify({
        "message": "Login successful!",
        "user": {
            "id": user.id,
            "name": user.name,
            "email": user.email
        }
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
