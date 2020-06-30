from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from hashlib import md5

@login.user_loader
def loadUser(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)

    status = db.Column(db.String(20), index = True)
    username = db.Column(db.String(50), index = True, unique = True)
    email = db.Column(db.String(60), index = True, unique = True)
    password_hash = db.Column(db.String(128))

    name = db.Column(db.Text, index=True)
    surname = db.Column(db.Text, index=True)
    town = db.Column(db.Text, index=True)
    about = db.Column(db.Text, index=True)

    good_comments = db.relationship('GoodComment', backref='author', lazy="dynamic")
    basket = db.relationship('Basket', backref='author', lazy="dynamic")

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def setPassword(self, password):
        self.password_hash = generate_password_hash(password)

    def checkPassword(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)