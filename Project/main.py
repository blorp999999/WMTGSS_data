from flask import Flask, render_template, request, redirect, url_for, Blueprint
from flask_login import login_required, current_user
from . import db
import pytest


'''
def index
Basic Flask index function, returns index page of website
'''
@Flask.main.route('/')
def index():
    return render_template('index.html')

@Flask.main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name = current_user.name)
    
