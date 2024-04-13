from flask import Blueprint
from flask import render_template
from flask import jsonify
import os

system_bp = Blueprint("system", __name__)


@system_bp.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@system_bp.route("/health", methods=["GET"])
def health():
    return (
        jsonify({"health": "ok", "DOCKER_REPOSITORY": os.getenv("DOCKER_REPOSITORY", "unknown"), "DOCKER_IMAGE_TAG": os.getenv("DOCKER_IMAGE_TAG", "unknown")})
    )
