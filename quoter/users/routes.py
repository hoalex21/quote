from functools import wraps

from flask import Blueprint, redirect, url_for, render_template
from flask_login import current_user, login_user, login_required, logout_user

from quoter import login_manager, bcrypt, db
from quoter.models.user import User

from .forms import RegisterForm, LoginForm

users = Blueprint("users", __name__)


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()

def logout_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.is_authenticated:
            return redirect(url_for("root.index"))
        return f(*args, **kwargs)
    return decorated_function

@users.route("/register", methods=["GET", "POST"])
@logout_required
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        email = form.email.data
        username = form.username.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(email=email, username=username, first_name=first_name, last_name=last_name, password=password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("root.index"))
    return render_template("users/register.html", form=form)

@users.route("/login", methods=["GET", "POST"])
@logout_required
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user, form.remember.data)
                return redirect(url_for("root.index"))
            else:
                # TODO: Handle incorrect password
                pass
        else:
            # TODO: Handle incorrect username
            pass
    return render_template("users/login.html", form=form)

@users.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    logout_user()
    return render_template("users/logout.html")

@users.route("/profile/<username>")
def profile(username):
    user = User.query.filter_by(username=username).first()
    return render_template('users/profile.html', user=user, username=username)
