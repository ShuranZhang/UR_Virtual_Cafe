from flask.helpers import flash
from project.forms import PostForm
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
    return render_template('forum.html', name=current_user.name, posts=posts)

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', current_user=current_user)

@main.route("/post/new",methods=['GET','POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data,author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!','success')
        return redirect(url_for('main.forum'))
    return render_template('create_post.html',title='New Post',name=current_user.name, form=form)

