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
    age = db.Column(db.String(3))
    notes = db.relationship('Note')
    books = db.relationship('Book')

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    doctor = db.Column(db.String(20))
    issue = db.Column(db.String(50))
    clinic = db.Column(db.String(20))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))