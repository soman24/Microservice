from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import SubmitField, EmailField
from wtforms.validators import DataRequired


class Form(FlaskForm):
    text_file = FileField('Text File', validators=[FileRequired(), FileAllowed(['txt'], 'Text File only!')])
    email = EmailField('Email', validators=[DataRequired()])
    submit = SubmitField('Submit')