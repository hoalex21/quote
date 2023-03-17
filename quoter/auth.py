from flask import Blueprint

bp = Blueprint("auth", __name__)


@bp.route("/register")
def register():
    return "<h1>auth.register</h1>"

@bp.route("/login")
def login():
    return "<h1>auth.login</h1>"

@bp.route("/logout")
def logout():
    return "<h1>auth.logout</h1>"
