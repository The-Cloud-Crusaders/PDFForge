from flask import Blueprint
from flask import render_template


system_bp = Blueprint("system", __name__)


@system_bp.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@system_bp.route("/health", methods=["GET"])
def health():
    return "OK", 200
