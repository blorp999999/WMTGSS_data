from flask import Flask, render_template, request, redirect, url_for, Blueprint
from . import db


'''
def index
Basic Flask index function, returns index page of website
'''
@Flask.main.route('/')
def index():
    return render_template('index.html')

@Flask.main.route('/profile')
def profile():
    return 'Profile'