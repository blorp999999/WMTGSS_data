from flask import Flask, render_template, request, redirect, url_for, Blueprint
from flask_sqlalchemy import SQLAlchemy
from main import app, db

auth = Blueprint('auth', __name__)

@app.route('/profile')
def profile():
    return 'Profile'

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('logout')
def logout():
    return 'Logout'
    