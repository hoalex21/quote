from flask import Blueprint, render_template
from flask_login import login_required, current_user

from quoter import db
from quoter.models.post import Post
from quoter.models.user import User

from .forms import CreateForm

posts = Blueprint('posts', __name__)


@login_required
@posts.route('/post', methods=["GET", "POST"])
def create():
    form = CreateForm()

    if form.validate_on_submit():
        content = form.content.data
        post = Post(content=content, user_id=current_user.id)
        db.session.add(post)
        db.session.commit()

    return render_template("posts/create.html", form=form)

@posts.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.filter_by(id=post_id).first()

    if post:
        user = User.query.filter_by(id=post.user_id).first()
        return render_template("posts/post.html", post=post, user=user, post_id=post_id)

    return render_template("posts/post.html", post=post, post_id=post_id)
