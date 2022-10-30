from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User,Rel
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user





auth = Blueprint('auth',__name__)

@auth.route('/login', methods=["GET","POST"])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        print(user)
        if user:
            if check_password_hash(user.password, password):
                if email[-9:]=="admin.com":
                    flash('Logged in succesfully!', category='success')
                    login_user(user, remember=True)
                    return redirect(url_for('views.admin'))
                else:
                    flash('Logged in succesfully!', category='success')
                    login_user(user, remember=True)
                    return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category="error")
        else:
            flash('Email does not exist', category="error")

    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out succesfully!', category="success")
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=["GET","POST"])
def sign_up():
    if request.method == "POST":
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        age = request.form.get('age')
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash("Email must be greater than 4 characters.", category="error")
        elif len(first_name) < 2:
            flash("First Name must be greater than 2 characters.", category="error")
        elif password1 != password2:
            flash("Passwords don't match.", category="error")
        elif len(password1) < 7:
            flash("Password must be at least 7 characters.", category="error")
        elif len(age) > 2:
            flash("Age cannot be more than 2 characters.", category="error")
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method="sha256"),age=age,rel_id=1)
            db.session.add(new_user)
            db.session.commit()
            #new_user1 = Rel(id=1,)
            #db.session.add(new_user1)
            #db.session.commit()
            if email[-9:]=="admin.com":
                login_user(new_user, remember = True)
                flash("Account created!", category="success")
                return redirect(url_for('views.admin'))

            else:
                login_user(new_user, remember = True)
                flash("Account created!", category="success")
                return redirect(url_for('views.home'))
            #add user to database
    return render_template("sign_up.html", user=current_user)