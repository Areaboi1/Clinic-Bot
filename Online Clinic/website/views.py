import json
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_user, login_required, logout_user, current_user
from .models import Book, Note, User, Rel
from . import db
from datetime import date
import mysql.connector

db1=mysql.connector.connect(user='root', passwd='12345678',
                              host='localhost',
                              database='Book')
mycurs=db1.cursor()
q1=""
views = Blueprint('views',__name__)

@views.route('/', methods=['GET','POST'])
@login_required
def home():
    if request.method == "POST":
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short', category="error")
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note was created', category="success")
    return render_template("home.html", user=current_user)

@views.route('/delete-note', methods=["POST"])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    return jsonify({})

@views.route('/book', methods=['GET','POST'])
@login_required
def book():
    if request.method == "POST":
        issue = str(request.form.get("issue"))
        clinic = "Queenstown"
        doctor = str(request.form.get("doctor"))
        date = str(request.form.get("date"))
        time = str(request.form.get("time"))
        pname = str(request.form.get("pname"))
        #username = current_user.first_Name
        #email = current_user.email
        datetime= str(doctor) + str(date) + str(time)
        if len(issue) < 3:
            flash("Issue too short.", category="error")
        if len(pname) < 1:
            flash("Name too short.", category="error")
        elif type(doctor) != str:
            flash("Choose a doctor.", category="error")
        elif len(date) < 3:
            flash("Choose a date.", category="error")
        elif len(time) < 1 or len(time) > 2 or int(time)>24 or int(time)<1:
            flash("Choose a correct time.", category="error")
        else:
            time += ":00"
            new_book = Book(issue=issue, clinic=clinic, doctor=doctor, date=date, user_id=current_user.id,time=time,datetime=datetime,pname=pname)
            db.session.add(new_book)
            db.session.commit()
            #q1="INSERT INTO Book1 VALUES({a},{b},{c},{d},{e},{f},{g})".format(a=pname,b=date,c=time,d=clinic,e=doctor,f=issue,g=datetime)
            #mycurs.execute(q1)
            flash('Appointment was booked', category="success")
#    if request.method == "POST":
#       bookt = request.form.get('bookt')
#       user = User.query.filter_by(email=email).first()
#        if user:
#           flash('Not available.', category='error')
#       else:
#           new_note = Note(data=note, user_id=current_user.id)
# 
#           db.session.add(new_note)
#           db.session.commit()
#        flash('Appointment was booked.', category="success")
    return render_template("bookapp.html", user=current_user)

@views.route('/prof', methods=['GET','POST'])
@login_required
def prof():
    return render_template("profd.html", user=current_user)

@views.route('/viewapp', methods=['GET','POST'])
@login_required
def viewapp():
    return render_template("viewapp.html", user=current_user)

@views.route('/admin', methods=['GET','POST'])
@login_required
def admin():
    #user = User.query.filter_by(email=email).first()
    #print(user)
    return render_template("admin.html", user=current_user)

@views.route('/doc', methods=['GET','POST'])
@login_required
def doc():
    #user = User.query.filter_by(email=email).first()
    #print(user)
    return render_template("admin.html", user=current_user)

@views.route('/delete-book', methods=["POST"])
def delete_book():
    book = json.loads(request.data)
    bookId = book['bookId']
    book = Book.query.get(bookId)
    if book:
        if book.user_id == current_user.id:
            db.session.delete(book)
            db.session.commit()
    return jsonify({})
