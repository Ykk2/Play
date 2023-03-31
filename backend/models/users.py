import bcrypt
from .db import db
from flask_login import UserMixin


class User(UserMixin, db.model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    hashed_password = db.Column(db.String(300), nullable=False, unique=True)

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        print("inside the password setter")
        salt = bcrypt.gensalt()
        self.hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)

    def check_password(self, password):
        return bcrypt.checkpw(self.password.encode("utf-8"), password)

    def to_json(self):
        keys = ["id", "username", "email"]
        return {key: value for key, value in vars(self).items() if key in keys}
