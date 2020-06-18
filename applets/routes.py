from applets import app
from flask import request, render_template, redirect, url_for, flash


# HOME PAGE
@app.route('/', methods=['GET'])
def index():
    # Example parameters
    # This is where your functions from python come from
    variables = ['This is variable one', 'This is variable two']
    return render_template('index.html', variables=variables)
