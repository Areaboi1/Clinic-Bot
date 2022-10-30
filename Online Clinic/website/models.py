from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')
    age = db.Column(db.String(3))
    books = db.relationship('Book')
    rel_id = db.Column(db.Integer, db.ForeignKey('rel.id'))


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(34))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    issue = db.Column(db.String(30))
    doctor = db.Column(db.String(30))
    datetime = db.Column(db.String(50),unique=True)
    time = db.Column(db.String(6))
    clinic = db.Column(db.String(30))

class Rel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    users = db.relationship('User')

