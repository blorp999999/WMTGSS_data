from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


# Init application as a Flask app (used in other files/modules)
app = Flask(__name__)

# init SQLAlchemy for later use
db = SQLAlchemy()

'''
def index
Basic Flask index function, returns index page of website
'''
@app.route('/')
def index():
    return render_template('index.html')