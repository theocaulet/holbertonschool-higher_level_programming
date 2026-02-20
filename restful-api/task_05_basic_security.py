#!/usr/bin/python3
"""Flask app demonstrating Basic Auth and JWT-based protected routes."""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity,
    get_jwt
)
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

app = Flask(__name__)


app.config["JWT_SECRET_KEY"] = "super-secret-key"
jwt = JWTManager(app)
auth = HTTPBasicAuth()


users = {
    "admin": {
        "password": generate_password_hash("admin123"),
        "role": "admin"
    },
    "user": {
        "password": generate_password_hash("user123"),
        "role": "user"
    }
}


@auth.verify_password
def verify_password(username, password):
    """Verify user credentials for HTTP Basic authentication.

    Args:
        username: The username to verify.
        password: The plaintext password to check.

    Returns:
        The username if credentials are valid, None otherwise.
    """
    if username in users and check_password_hash(users[username]["password"],
                                                 password):
        return username
    return None


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """Return a greeting for an authenticated Basic Auth user."""
    return jsonify(message=f"Hello {auth.current_user()}! (Basic Auth)")


@app.route("/login", methods=["POST"])
def login():
    """Authenticate a user and return a JWT access token.

    Expects JSON with 'username' and 'password' fields.
    Returns the JWT access token with role claim on success.
    """
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username in users and check_password_hash(users[username]["password"],
                                                 password):
        access_token = create_access_token(
            identity=username,
            additional_claims={"role": users[username]["role"]}
        )
        return jsonify(access_token=access_token)

    return jsonify({"msg": "Bad username or password"}), 401


@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """Return a greeting for an authenticated JWT user."""
    current_user = get_jwt_identity()
    return jsonify(message=f"Hello {current_user}! (JWT Auth)")


def role_required(required_role):
    """Create a decorator that restricts access to a specific role.

    Args:
        required_role: The role required to access the decorated route.

    Returns:
        A decorator function that enforces role-based access control.
    """
    def wrapper(fn):
        """Wrap a view function with role-based JWT authorization."""
        @wraps(fn)
        def decorator(*args, **kwargs):
            """Check if the JWT user's role matches the required role."""
            claims = get_jwt()
            user_role = claims.get("role")

            if user_role != required_role:
                return jsonify({"msg": "Access forbidden: insufficient"
                                " permissions"}), 403

            return fn(*args, **kwargs)
        return decorator
    return wrapper


@app.route("/admin-only")
@jwt_required()
@role_required("admin")
def admin_route():
    """Return a response for authenticated users with admin role."""
    return jsonify(message="Welcome Admin!")


@app.route("/user-only")
@jwt_required()
@role_required("user")
def user_route():
    """Return a response for authenticated users with user role."""
    return jsonify(message="Welcome User!")


if __name__ == "__main__":
    app.run(debug=True)
