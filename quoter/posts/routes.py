from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user

from quoter import db
from quoter.models.post import Post
from quoter.models.user import User

from .forms import CreateForm, LikeForm, UnlikeForm

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
        return redirect(url_for("root.index"))

    return render_template("posts/create.html", form=form)

@posts.route("/post/<int:post_id>", methods=["GET", "POST"])
def post(post_id):
    post = Post.query.filter_by(id=post_id).first()

    form = None

    # Like/Unlike post
    if request.method == "POST":
        if current_user.is_authenticated:
            if current_user not in post.liked:
                current_user.likes.append(post)
            else:
                current_user.likes.remove(post)
            db.session.commit()
        else:
            # If no user is authenticated, redirect to register upon clicking Like button
            return redirect(url_for("users.register"))

    if post:
        user = User.query.filter_by(id=post.user_id).first()

        # Show Like/Unlike button depending on user's relationship with post
        if current_user.is_authenticated:
            if current_user in post.liked:
                form = UnlikeForm()
            else:
                form = LikeForm()

        return render_template("posts/post.html", post=post, user=user, post_id=post_id, form=form)

    return render_template("posts/post.html", post=post, post_id=post_id)
