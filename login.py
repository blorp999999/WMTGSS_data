from flask import Flask, render_template, request, redirect, url_for, Blueprint
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from models import User
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
    
@auth.route('/signup', methods=['POST'])
def signup_post():
    
    # Validates and adds user to the database
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    
    user = User.query.filter_by(email=email).first() # Checks if the user email is already within the database
    
    if user: # If the user already exists, redirect back to the signup page so the user can try again
        return redirect(url_for('auth.signup'))
    
    # Creates a new user with the form data
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256')) # Hashes the password so a plaintext version isn't saved
    
    # Add the new user to the database
    db.session.add(new_user)
    db.session.commit()
    
    
    # Once signup is completed, redirects the user to the login page
    return redirect(url_for('auth.login'))

@auth.route('logout')
def logout():
    return 'Logout'
    