import os
import json

interface_file = os.path.join(os.path.dirname(__file__), 'interface.json')
with open(interface_file, 'r') as outfile:
    interface = json.load(outfile)

store_file = os.path.join(os.path.dirname(__file__), 'database', 'stores.json')
with open(store_file, 'r') as outfile:
    store_db = json.load(outfile)

item_file = os.path.join(os.path.dirname(__file__), 'database', 'items.json')
with open(item_file, 'r') as outfile:
    items_db = json.load(outfile)


class Config(object):
    # Flask Framework
    HOST = '0.0.0.0'
    PORT = 8000
    DEBUG = True
    SECRET_KEY = '1234'

    # User Interface
    TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), 'templates')
    STATIC_PATH = os.path.join(os.path.dirname(__file__), 'static')
    INTERFACE = interface
    STOREDB = store_db
    ITEMSDB = items_db
