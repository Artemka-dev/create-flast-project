a = ["""from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = "login"

from app import routes, models""", """from app import app, db
from flask import render_template, request, url_for, redirect, flash
from flask_login import current_user, login_user, logout_user, login_required
from app.models import *
from app.forms import LoginForm, RegistrationForm

@app.route("/")
def main():
    return 'Hello world'""", """from flask_wtf import FlaskForm
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
    submit = SubmitField('')""", """from app import app

if __name__ == "__main__":
    app.run(debug=True)""", """import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'try_to_guess'""", """from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from hashlib import md5

@login.user_loader
def loadUser(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(50), index = True, unique = True)
    email = db.Column(db.String(60), index = True, unique = True)
    password_hash = db.Column(db.String(128))

    name = db.Column(db.Text, index=True)
    surname = db.Column(db.Text, index=True)
    town = db.Column(db.Text, index=True)
    about = db.Column(db.Text, index=True)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def setPassword(self, password):
        self.password_hash = generate_password_hash(password)

    def checkPassword(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)""", """flask

flask-wtf
flask-migrate
flask-sqlalchemy
flask-login
flask-mail""", """<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <!-- <link rel="shortcut icon" href="{{ url_for('static', filename='img/...png') }}">
    <script src="https://www.google.com/recaptcha/api.js" async defer></script>
    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename = 'css/bootstrap.css') }}">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css"
        integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">
    <script src="{{ url_for('static', filename = 'js/jquery-3.3.1.min.js') }}"></script>
    <script src="{{ url_for('static', filename = 'js/popper.js') }}"></script>
    <script src="{{ url_for('static', filename = 'js/bootstrap.js') }}"></script>
    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/master.css') }}"> -->
</head>
<body></body>
</html>"""]