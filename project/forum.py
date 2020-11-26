from flask import Blueprint, render_template, redirect, url_for, request, flash
from project.forms import PostForm
from project.models import Post
from flask_login import login_user, logout_user, login_required, current_user
from . import db

forum = Blueprint('forum', __name__)

@forum.route("/post/new",methods=['GET','POST'])
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

