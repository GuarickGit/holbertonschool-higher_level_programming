#!/usr/bin/env python3

from flask import Flask
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager
from flask import request
from flask import jsonify
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity

# Initialisation de l'application Flask
app = Flask(__name__)
auth = HTTPBasicAuth()

# Clé secrète utilisée pour signer les tokens JWT
app.config["JWT_SECRET_KEY"] = "super-secret-key"
jwt = JWTManager(app)

# Gestion des erreurs JWT : renvoyer un message et un code 401 dans chaque cas
@jwt.unauthorized_loader
def handle_missing_token(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token(jwt_header, jwt_payload):
    return jsonify({"error": "Fresh token required"}), 401

# Base de données simulée en mémoire contenant les utilisateurs
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}


@auth.verify_password
def verify_password(username, password):
    """
    Vérifie les identifiants pour l'authentification HTTP Basic.
    """
    if username in users and \
            check_password_hash(users[username]["password"], password):
        return username

@app.route('/basic-protected')
@auth.login_required
def index():
    """
    Route protégée par authentification HTTP Basic.
    Accessible uniquement avec des identifiants valides.
    """
    return "Basic Auth: Access Granted"

@app.route('/login', methods=["POST"])
def login():
    """
    Route de connexion pour générer un token JWT.
    Reçoit un JSON avec username et password.
    Retourne un token si les identifiants sont valides.
    """
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    identity = {
    "username": username,
    "role": users[username]["role"]
    }

    if username in users and \
            check_password_hash(users[username]["password"], password):
        access_token = create_access_token(identity=identity)

        return jsonify(access_token=access_token), 200

    else:
        return jsonify({"error": "Invalid credentials"}), 401


@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    """
    Route protégée par JWT.
    Nécessite un token valide dans l'en-tête Authorization.
    """
    return "JWT Auth: Access Granted"

@app.route('/admin_only')
@jwt_required()
def is_admin():
    """
    Route protégée par JWT + vérification de rôle.
    Accessible uniquement si le rôle est 'admin'.
    """
    identity = get_jwt_identity()
    if identity.get("role") == "admin":
        return "Admin Access: Granted", 200

    else:
        return jsonify({"error": "Admin access required"}), 403


if __name__ == '__main__':
    # Démarre le serveur Flask en local
    app.run()
