from app import app, db
from flask import render_template, request, url_for, redirect, flash
from flask_login import current_user, login_user, logout_user, login_required
from app.models import *
from app.forms import LoginForm, RegistrationForm

@app.route("/")
def main():
    return 'Hello world'