import os


class Config(object):
    # Flask Framework
    HOST = '0.0.0.0'
    PORT = 5080
    DEBUG = True
    SECRET_KEY = '1234'

    # User Interface
    TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), 'templates')
    STATIC_PATH = os.path.join(os.path.dirname(__file__), 'static')
