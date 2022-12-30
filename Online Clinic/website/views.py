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
        email = current_user.email
        datetime= str(doctor) + str(date) + str(time)
        date1 = Book.query.filter_by(datetime=datetime).first()
        print(date1)
        if date1:
            flash("Choose another date and time.", category="error")
        elif len(issue) < 3:
            flash("Issue too short.", category="error")
        elif len(pname) < 1:
            flash("Name too short.", category="error")
        elif type(doctor) != str:
            flash("Choose a doctor.", category="error")
        elif len(date) < 3:
            flash("Choose a date.", category="error")
        elif len(time) < 1 or len(time) > 2 or int(time)>24 or int(time)<1:
            flash("Choose a correct time.", category="error")
            if len(time)==1:
                time="0"+time
        else:
            time += ":00"
            #inset a query filter
            q1="INSERT INTO Book1 VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
            val=(pname,date,time,clinic,doctor,issue,datetime,email)
            mycurs.execute(q1,val)
            db1.commit()
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
    if request.method == "POST":
        doctor = [str(request.form.get("doctor")),]
        str(len(doctor[0]))
        if str(doctor[0])=="None":
                    qu1="Select * from Book1"
                    mycurs.execute(qu1,)
                    data2=mycurs.fetchall()

        else:
            qu1="Select * from Book1 where Doctor=%s"
            mycurs.execute(qu1,doctor)
            data2=mycurs.fetchall()

    else:
        qu1="Select * from Book1"
        mycurs.execute(qu1,)
        data2=mycurs.fetchall()
    return render_template("admin.html", user=current_user,data2=data2)

@views.route('/doc', methods=['GET','POST'])
@login_required
def doc():
    #user = User.query.filter_by(email=email).first()
    #print(user)
    if request.method == "POST":
        val = (current_user.first_name,str(request.form.get("date")))
        print(len(str(val[1])))
        if str(val[1])=="":
                    qu1="Select * from Book1 where Doctor=%s"
                    val=(current_user.first_name,)
                    mycurs.execute(qu1,val)
                    data1=mycurs.fetchall()

        else:
            qu1="Select * from Book1 where Doctor=%s and Bdate=%s"
            mycurs.execute(qu1,val)
            data1=mycurs.fetchall()

    else:
        qu1="Select * from Book1 where Doctor=%s"
        val=(current_user.first_name,)
        mycurs.execute(qu1,val)
        data1=mycurs.fetchall()

    return render_template("doc.html", user=current_user,data1=data1)

@views.route('/delete-book', methods=['GET',"POST"])
def delete_book():
    book = json.loads(request.data)
    bookId = book['bookId']
    #datetime = book['datetime']
   # print(date1)
    book = Book.query.get(bookId)
    if book:
        date1=[book.datetime,]
        print(type(date1))
        q1="DELETE FROM Book1 where datetime1=%s"
        mycurs.execute(q1,date1)
        db1.commit()
        db.session.delete(book)
        db.session.commit()
    return jsonify({})
