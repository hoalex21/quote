from flask import Blueprint, render_template

from quoter.models.post import Post
from quoter.models.user import User

root = Blueprint("root", __name__)


@root.route("/")
def index():
    posts = Post.query.all()

    return render_template("root/index.html", posts=posts)
