from flask import Flask, render_template, request, redirect, url_for, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os
import pytest


# Init application as a Flask app (used in other files/modules)
app = Flask(__name__)

# init SQLAlchemy for later use
db = SQLAlchemy()
dbf = SQLAlchemy()

UPLOAD_DIRECTORY = '/WMGTSS_uploaded_files'

# Check if the file storage location exists, if it does not, creates it
#if not os.path.exists(UPLOAD_DIRECTORY):
    #os.makedirs(UPLOAD_DIRECTORY)


def create_app():
    from flask import Flask

    app = Flask(__name__)
    
    app.config['MAX_CONTENT_LENGTH'] = 200 * 1024 * 1024 # Security feature, limits the filesize of uploaded files to 200MB to prevent server overload through upload of massive files
    app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.mp4', '.doc', '.docx', '.pdf', '.odt', '.html', '.ppt', '.pptx'] # Security feature, limits allowed files to previously specified ones (prevents upload of code files, etc)
    app.config['UPLOAD_PATH'] = 'uploads'
    app.config['SECRET_KEY'] = 'put_secret_key_here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://db.sqlite'
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    from .models import User 
    
    @login_manager.user_loader
    def load_user(user_id):
        # Since user id is the primary key of the database, more efficient to query using that
        return User.query.get(int(user_id)) # User ID is meant to be an integer, but best to confirm
    
    
    db.init_app(app)
    
    from .login import auth as ab 
    #app.register_blueprint(ab)
    

    #app.register_blueprint(Flask.main)
    
    return app

if __name__ == '__init__':
    app.run() # Runs Flask app