import json
import datetime
from flask import Flask
from config import Config
from bson.objectid import ObjectId


class JSONEncoder(json.JSONEncoder):
    ''' extend json-encoder class'''
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, datetime.datetime):
            return str(o)
        return json.JSONEncoder.default(self, o)


app = Flask(__name__)
app.config.from_object(Config)
app.template_folder = app.config['TEMPLATE_PATH']
app.static_folder = app.config['STATIC_PATH']
app.json_encoder = JSONEncoder


from applets import routes
