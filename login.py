from flask import Flask, render_template, request, redirect, url_for, Blueprint, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import app, db
from flask_login import login_user, login_required, logout_user

auth = Blueprint('auth', __name__)

@app.route('/profile')
def profile():
    return 'Profile'

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    # Login code
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    
    user = User.query.filter_by(email=email).first()
    
    # Checks if the user actually exists
    # Takes password entered, hashes it, and compares it to hashed version within database
    if not user or not check_password_hash(user.password, password):
        flash('Incorrect username or password, please check your login details and try again.')
        return redirect(url_for('auth.login')) # If user doesn't exist, or password is incorrect, redirects back to login page
    
    login_user(user, remember=remember) # Creates a user session
    # If all of the above passes, we know the user has the right credentials
    return redirect(url_for('main.profile'))

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
        flash('This email address is already being used, please create an account with another email address') # Informs user that the email is already present if they enter a previously used email
        return redirect(url_for('auth.signup'))
    
    # Creates a new user with the form data
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256')) # Hashes the password so a plaintext version isn't saved
    
    # Add the new user to the database
    db.session.add(new_user)
    db.session.commit()
    
    
    # Once signup is completed, redirects the user to the login page
    return redirect(url_for('auth.login'))

@auth.route('logout')
@login_required
def logout():
    # Logs the user out
    logout()
    return redirect(url_for('main.index')) # Returns user to main page/index