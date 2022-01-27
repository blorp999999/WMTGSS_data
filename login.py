from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from main import app, db

auth = Blueprint('auth', __name__)

@app.route('/profile')
def profile():
    return 'Profile'

@auth.route('/login')
def login():
    return 'Login'

@auth.route('/signup')
def signup():
    return 'Signup'

@auth.route('logout')
def logout():
    return 'Logout'
    