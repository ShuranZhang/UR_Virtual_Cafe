from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User
from wtforms.widgets import TextArea

class PostForm(FlaskForm):
    title = StringField('Title',validators=[DataRequired()])
    content = StringField('Content',validators=[DataRequired()], widget=TextArea())
    submit = SubmitField('Post')