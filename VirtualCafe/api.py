from flask import render_template, redirect, request,url_for, Blueprint
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from .forms import SignUpForm, LogInForm
from .models import User
from . import db

app = Blueprint('api', __name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('index', _external=True))
    form = SignUpForm()
    if form.validate_on_submit():
        enc_pass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        newuser = User(username=form.username.data, email=form.email.data, password=enc_pass)
        db.session.add(newuser)
        db.session.commit()
        return redirect(url_for('login', _external=True))
    return render_template('signup.html', form=form)

    
@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index', _external=True))
    form = LogInForm()
    if form.validate_on_submit():
        user = user.query.get(email = form.email.data)
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            return redirect(url_for('index', _external=True)) 
        else:
            flash("Login Failed. Please try again")
    return render_template('login.html', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home', _external=True))