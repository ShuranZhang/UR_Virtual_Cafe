from flask.helpers import flash
from project.models import Post
from flask import Blueprint, render_template, url_for, flash, redirect, request, abort
from flask_login import login_required, current_user
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/forum')
@login_required
def forum():
    posts = Post.query.all()
    return render_template('forum.html', posts=posts, current_user=current_user)

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', current_user=current_user)
