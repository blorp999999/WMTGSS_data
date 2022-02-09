from Project import create_app
from flask import Flask, render_template, request, redirect, url_for, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os
import pytest

def test_home_page():
    '''
    
    Tests the working of the Flask app through the following logic:
    
    GIVEN a flask app 
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    '''
    
    flask_app = create_app()
    
    # Create a test client using the Flask app
    with flask_app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200