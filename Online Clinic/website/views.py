from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_user, login_required, logout_user, current_user
from .models import Note, Book
from . import db
import json



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
        issue = request.form.get("issue")
        clinic = request.form.get("clinic")
        doctor = request.form.get("doctor")
        date = request.form.get("date")
        if len(issue) < 3:
            flash("Issue too short.", category="error")
        elif type(clinic) != str:
            flash("Choose a clinic.", category="error")
        elif type(doctor) != str:
            flash("Choose a doctor.", category="error")
        elif len(date) < 3:
            flash("Choose a date.", category="error")
        else:
            new_book = Book(issue=issue, clinic=clinic, doctor=doctor, date=date, user_id=current_user.id)
            db.session.add(new_book)
            db.session.commit()
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

@views.route('/cancel', methods=['GET','POST'])
@login_required
def cancel():
    return render_template("cancelapp.html", user=current_user)

@views.route('/v', methods=['GET','POST'])
@login_required
def v():
    return render_template("view.html", user=current_user)