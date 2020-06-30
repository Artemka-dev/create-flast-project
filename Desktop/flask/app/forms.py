from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Length

class LoginForm(FlaskForm):
    username = StringField('', validators=[DataRequired()])
    password = PasswordField('', validators=[DataRequired()])
    submit = SubmitField('')

class RegistrationForm(FlaskForm):
    username = StringField('', validators=[DataRequired()])
    email = StringField('', validators=[DataRequired()])
    password1 = PasswordField('', validators=[DataRequired()])
    password2 = PasswordField('', validators=[DataRequired(), EqualTo('password1')])
    submit = SubmitField('')