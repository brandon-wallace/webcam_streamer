# application/__init__.py

from os import environ
from flask import Flask

app = Flask(__name__)


def create_app():
    '''Initialize application'''

    app.config['DEBUG'] = False
    app.config['FLASK_ENV'] = environ.get('FLASK_ENV')
    app.config['SECRET_KEY'] = environ.get('SECRET_KEY')

    from application import routes

    return app
