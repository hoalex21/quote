from flask import Blueprint, redirect, url_for, render_template
from flask_login import current_user, login_user, login_required, logout_user

from quoter import login_manager, bcrypt, db
from quoter.models import User

from .forms import RegisterForm, LoginForm

auth = Blueprint("auth", __name__)


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()

@auth.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if not current_user.is_authenticated:
        if form.validate_on_submit():
            email = form.email.data
            username = form.username.data
            first_name = form.first_name.data
            last_name = form.last_name.data
            password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user = User(email=email, username=username, first_name=first_name, last_name=last_name, password=password)
            db.session.add(user.id)
            db.session.commit()
            return redirect(url_for("root.index"))
    return render_template("auth/register.html", form=form)

@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if not current_user.is_authenticated:
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user is not None:
                if bcrypt.check_password_hash(user.password, form.password.data):
                    login_user(user)
                else:
                    # TODO: Handle incorrect password
                    pass
            else:
                # TODO: Handle incorrect username
                pass
                return redirect(url_for("root.index"))
    return render_template("auth/login.html", form=form)

@auth.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    logout_user()
    return render_template("auth/logout.html")
