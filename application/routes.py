# application/routes.py

import cv2
from flask import render_template, Response
from application import app


video = cv2.VideoCapture(0)


@app.route('/')
def index():
    '''Index page'''

    return render_template('index.html')


def generator(webcam):
    '''Get camera frames'''

    while True:
        success, image = video.read()
        if success:
            ret, jpeg = cv2.imencode('.jpg', image)
            frame = jpeg.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/stream')
def video_stream():
    '''Display video stream'''

    return Response(generator(video),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.errorhandler(404)
def page_not_found(error):
    '''404 page not found route'''

    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    '''500 page not found route'''

    return render_template('500.html'), 500
