# application/routes.py

from flask import render_template, Response
from application import app
from application.camera import Camera


@app.route('/')
def index():
    return render_template('index.html')


def generator(webcam):
    '''Get camera frames'''

    while True:
        frame = webcam.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/stream')
def video_stream():
    '''Display video stream'''

    return Response(generator(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
