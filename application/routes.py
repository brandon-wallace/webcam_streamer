# application/routes.py

import os
import time
import threading
from flask import render_template, Response, request
from application import app


@app.route('/')
def index():
    return render_template('index.html')
    
    
def generator(webcam):
    '''Get camera frames'''
    
    while True:
        frame = None
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
               
               
@app.route('/stream')
def video_stream():
    '''Display video stream'''
    
    return Response(generator(camera), mimetype='multipart/x-mixed-replace; boundary=frame')
