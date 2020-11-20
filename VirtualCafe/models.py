from datetime import datetime
from . import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

class User(db.Model, UserMixin):
	__tablename__ ="user"
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(50), unique=True, nullable=False)
	email = db.Column(db.String(200), unique=True, nullable=False)
	password = db.Column(db.String(60), nullable=False)
	date_entry = db.Column(db.DateTime, default = datetime.utcnow)
#	posts = db.relationship('Post',backref='author', lazy=True)

	def __repr__(self):
		return f"User('{self.username}','{self.email}','{self.image_file}')"

#class Post(db.Model):