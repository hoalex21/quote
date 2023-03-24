from flask import Blueprint, redirect, url_for, render_template

from quoter import login_manager, bcrypt, db
from quoter.models import User

from .forms import RegisterForm

auth = Blueprint("auth", __name__)


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@auth.route("/register", methods=["GET", "POST"])
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
        print("Hi", User.query.all())
        return redirect(url_for("root.index"))
    return render_template("auth/register.html", form=form)

@auth.route("/login", methods=["GET", "POST"])
def login():
    pass

@auth.route("/logout", methods=["GET", "POST"])
def logout():
    pass
