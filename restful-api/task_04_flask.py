#!/usr/bin/python3
"""Flask API module."""

import json
from flask import Flask, jsonify, request


app = Flask(__name__)

users = {}


@app.route('/')
def home():
    """Display the API welcome message."""
    return 'Welcome to the Flask API!'


@app.route('/data')
def data():
    """Return the API status."""
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    """Return all usernames."""
    return ('OK')


@app.route("/users/<username>")
def get_user(username):
    """Return one user by username."""
    if username in users:
        return users[username], 200
    return {"error": "User not found"}, 404


@app.route("/add_user", methods=['POST'])
def add_user():
    """Add a new user from JSON data."""
    try:
        user_data = json.loads(request.get_data())
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid JSON"}), 400

    if not user_data or "username" not in user_data:
        return jsonify({"error": "Username is required"}), 400

    username = user_data["username"]

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = {
        "username": user_data.get("username"),
        "name": user_data.get("name"),
        "age": user_data.get("age"),
        "city": user_data.get("city")
    }
    return jsonify({"message": "User added", "user": users[username]}), 201


if __name__ == "__main__":
    app.run(debug=True)
