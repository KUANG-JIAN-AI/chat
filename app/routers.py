from flask import Blueprint, jsonify, render_template

from app.controllers.user import login

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def index():
    return render_template("index.html")

@main_bp.route("/login", methods=["POST"])
def login_user():
    return jsonify(login())