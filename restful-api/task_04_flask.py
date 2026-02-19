#!/usr/bin/python3
"""Simple Flask API with in-memory user management endpoints."""

from flask import Flask, jsonify, request

app = Flask(__name__)


dict_users = {}


@app.route("/")
def home():
    """Return a welcome message for the API root endpoint."""
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    """Return a JSON list of all usernames currently stored."""
    return jsonify(list(dict_users.keys()))


@app.route("/status")
def status():
    """Return a simple health status message."""
    return "OK"


@app.route("/users/<username>")
def users(username):
    """Return the user object for a username or a 404 error."""
    user = dict_users.get(username)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.route("/add_user", methods=["POST"])
def add_user():
    """Create a user from JSON payload with validation checks."""
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    if username in dict_users:
        return jsonify({"error": "Username already exists"}), 409

    user_data = data.copy()
    dict_users[username] = user_data

    return jsonify(
        {"message": "User added", "user": {username: user_data}}
    ), 201


if __name__ == "__main__":
    app.run()
