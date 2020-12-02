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
        return redirect(url_for('main.forum', _external=True))
    return render_template('create_post.html',title='New Post',name=current_user.name, form=form)


@forum.route('/post/update/<int:id>', methods = ['POST', 'GET'])
@login_required
def update_post(id):
    post = Post.query.get_or_404(id)
    form = PostForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            post.title = form.title.data
            post.content = form.content.data
            db.session.add(post)
            db.session.commit()
            flash('Your post has been updated!')        
        return redirect(url_for('main.forum', _external=True))
    else:
        return render_template('update_post.html', current_user=current_user, post=post, form=form)

@forum.route('/post/delete/<int:id>', methods = ['POST', 'GET'])
@login_required
def delete_post(id):
    post = Post.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('main.forum', _external=True))