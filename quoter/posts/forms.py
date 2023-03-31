from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField


class CreateForm(FlaskForm):
    content = TextAreaField()
    submit = SubmitField("Post")

class LikeForm(FlaskForm):
    submit = SubmitField("Like")

class UnlikeForm(FlaskForm):
    submit = SubmitField("Unlike")
