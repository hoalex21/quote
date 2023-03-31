from flask_login import UserMixin

from quoter import db


like_post = db.Table(
    "like_post",
    db.Column("user_id", db.ForeignKey('user.id'), primary_key=True),
    db.Column("post_id", db.ForeignKey('post.id'), primary_key=True),
)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)
    username = db.Column(db.String, unique=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    password = db.Column(db.String)
    posts = db.relationship('Post', backref='user')
    likes = db.relationship('Post', secondary=like_post, backref='liked')
