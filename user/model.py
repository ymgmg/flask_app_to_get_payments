from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(150))
    role = db.Column(db.String(10))

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f"<User_id: {self.id}, email: {self.email}>"
