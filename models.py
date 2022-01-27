from . import db
from flask_login import UserMixin

class User(UserMixin, db.model):
    id = db.Column(db.Integer, primary_key=True) # User ID, used as the primary key within the user database
    email = db.Column(db.String, unique=True) # User Email, has to be unique
    password = db.Column(db.String(100)) # User Password, has to be hashed
    name = db.Column(db.String(1000)) # User name