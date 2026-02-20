#!/usr/bin/python3
"""Flask app demonstrating Basic Auth and JWT-based protected routes."""

from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity, get_jwt
)
from functools import wraps

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config["JWT_SECRET_KEY"] = "secret-key"
jwt = JWTManager(app)

users = {
        "admin": generate_password_hash("admin"),
        "user": generate_password_hash("user")
        }


@auth.verify_password
def verify_password(username, password):
    """Validate user credentials for HTTP Basic authentication."""
    if username in users and \
            check_password_hash(users.get(username), password):
        return username


@app.route('/')
@auth.login_required
def index():
    """Return a greeting for an authenticated Basic Auth user."""
    return f"Hello, {auth.current_user()}!"


@app.route('/login', methods=['POST'])
def login():
    """Authenticate a user and return a JWT access token."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if username in users and check_password_hash(users[username], password):
        access_token = create_access_token(
            identity=username,
            additional_claims={"role": username}
        )
        return jsonify(access_token=access_token), 200
    return jsonify({"msg": "Bad username or password"}), 401


@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    """Return a greeting for an authenticated JWT user."""
    current_user = get_jwt_identity()
    return jsonify(message=f"Hello, {current_user}! (JWT Auth)"), 200


def role_required(role):
    """Create a decorator that restricts access to users with a given role."""
    def wrapper(func):
        """Wrap a view function with role-based JWT authorization."""
        @wraps(func)
        @jwt_required()
        def decorator(*args, **kwargs):
            """Authorize request by matching JWT role claim."""
            claims = get_jwt()
            if claims.get("role") != role:
                return jsonify({"msg": "Forbidden"}), 403
            return func(*args, **kwargs)
        return decorator
    return wrapper


@app.route('/admin', methods=['GET'])
@jwt_required()
@role_required("admin")
def admin():
    """Return a response for authenticated users with admin role."""
    return jsonify(message="Welcome, admin!"), 200


@app.route('/user', methods=['GET'])
@jwt_required()
@role_required("user")
def user():
    """Return a response for authenticated users with user role."""
    return jsonify(message="Welcome, user!"), 200


if __name__ == '__main__':
    app.run(debug=True)
