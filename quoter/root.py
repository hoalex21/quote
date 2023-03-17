from flask import Blueprint

bp = Blueprint("root", __name__)


@bp.route("/")
def index():
    return "<h1>root.index</h1>"
