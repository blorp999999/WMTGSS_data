from flask import Flask, render_template, request, redirect, url_for, send_from_directory, jsonify
from flask_user import roles_required
from werkzeug.utils import secure_filename
import os
import imghdr
from . import app, UPLOAD_DIRECTORY
import pytest



'''
def validate_image
Takes uploaded image and validates it to ensure that it is non-malicious
Inputs: 
    - stream: Simple python stream input, takes data without use of callback (used over regular variables as is more efficiant)
Outputs:
    Outputs format of the file if has non-malicious data, if it is a malicious image, refuses to output it
'''
def validate_image(stream):
    header = stream.read(512)
    stream.seek(0)
    format = imghdr.what(None, header)
    if not format:
        return None
    return '.' + (format if format != 'jpeg' else 'jpg')
    
'''
def upload_files
Upload function, takes uploaded files, confirms whether they are of the correct filetype, and uploads them if everything is correct, then redirects to index page
'''
@app.route('/upload_form', methods=['GET', 'POST'])
@roles_required('Tutor') # Function is only available to users with a "Tutor" account
def upload_files():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        filename = secure_filename(uploaded_file.filename) # Uses the werkzeug secure_filename to reduce the filename of the uploaded to a flat filename - reduces vectors for filename based attacks
        if filename != '':
            file_ext = os.path.splitext(filename)[1]
            if file_ext not in app.config['UPLOAD_EXTENSIONS'] or file_ext != validate_image(uploaded_file.stream):
                Flask.abort(400) # If file is not in given filetypes, aborts and outputs a HTTP 400 error (bad request)
            
            uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
        return redirect(url_for('index'))
  
  
'''
def list_files
List endpoints for all files currently on the server
'''
@app.route('/files')
def list_files():
    files = []
    for filename in os.listdir(UPLOAD_DIRECTORY):
        path = os.path.join(UPLOAD_DIRECTORY, filename)
        if os.path.isfile(path):
            files.append(filename)
    return jsonify(files)
  
'''
def get_file
Performs a get request to download a specific file on the server
'''
@app.route('/files/<path:path>')
def get_file(path):
    # Download a file
    return send_from_directory(UPLOAD_DIRECTORY, path, as_attachment=True)