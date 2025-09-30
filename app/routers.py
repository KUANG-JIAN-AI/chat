from flask import Blueprint, jsonify, render_template

from app.controllers.msg import get_msg, send_msg
from app.controllers.user import get_friends, login

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    return render_template("index.html")


@main_bp.route("/login", methods=["POST"])
def login_user():
    return jsonify(login())


@main_bp.route("/friends", methods=["GET"])
def friends():
    return jsonify(get_friends())


@main_bp.route("/msg", methods=["POST"])
def msg():
    return jsonify(send_msg())


@main_bp.route("/msg", methods=["GET"])
def all_msg():
    return jsonify(get_msg())
