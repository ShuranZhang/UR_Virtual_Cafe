from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from .models import User
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login', _external=True)) # if the user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    return redirect(url_for('main.forum', _external=True))

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        flash('Email address already exists')
        return redirect(url_for('auth.signup', _external=True))

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login', _external=True))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

#Update user's account information
#If email already exist, it will flash a message
@auth.route('/update/<int:id>', methods = ['POST', 'GET'])
@login_required
def update(id):
    user = User.query.get_or_404(id)
    if request.method == 'POST':
        if request.form.get('email'):
            email = request.form.get('email')
            if User.query.filter_by(email=email).first() and current_user.email != email:
                flash('Email Update Failed - Email address already exists')
            else:
                user.email = email
        if request.form.get('name'):
            user.name = request.form.get('name')
        if request.form.get('oldpassword') and request.form.get('password'):
            oldpass = request.form.get('oldpassword')
            password = request.form.get('password')
            if check_password_hash(user.password, oldpass):
                flash('Password Updated')
                user.password = generate_password_hash(password, method='sha256')
            else:
                flash('Password Update Failed - Old passowrd does not match')
        db.session.commit()
        return redirect(url_for('main.profile', _external=True))
    else:
        return render_template('userupdate.html', user=user)

#delete a user account
@auth.route('/delete/<int:id>', methods = ['POST', 'GET'])
@login_required
def delete(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('auth.logout', _external=True))