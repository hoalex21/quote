from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField


class CreateForm(FlaskForm):
    content = TextAreaField()
    submit = SubmitField("Post")
