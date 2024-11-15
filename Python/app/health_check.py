from flask import Blueprint, jsonify

bp = Blueprint('health_check', __name__)


@bp.get("/health_check")
def review():
    return jsonify({"status": "OK"}), 200
