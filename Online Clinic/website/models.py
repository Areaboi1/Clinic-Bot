from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    age = db.Column(db.String(3))
    books = db.relationship('Book')
    email = db.Column(db.String(150))


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pname = db.Column(db.String(150))
    date = db.Column(db.String(34))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    issue = db.Column(db.String(30))
    doctor = db.Column(db.String(30))
    datetime = db.Column(db.String(50),unique=True)
    time = db.Column(db.String(6))
    clinic = db.Column(db.String(30))


