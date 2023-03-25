from flask_wtf import FlaskForm
from wtforms import EmailField, StringField, PasswordField, SubmitField, validators


class RegisterForm(FlaskForm):
    email = EmailField()
    username = StringField()
    first_name = StringField()
    last_name = StringField()
    password = PasswordField("Password", [validators.EqualTo("confirm_password", "Passwords must match.")])
    confirm_password = PasswordField()
    submit = SubmitField("Register")

class LoginForm(FlaskForm):
    email = EmailField()
    password = PasswordField()
    submit = SubmitField("Login")
