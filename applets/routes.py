from applets import app
from flask import request, render_template, redirect, url_for, flash
interface = app.config['INTERFACE']
stores = app.config['STOREDB']


# # HOME PAGE
# @app.route('/', methods=['GET'])
# def index():
#     # Example parameters
#     # This is where your functions from python come from
#     variables = ['This is variable one', 'This is variable two']
#     return render_template('index.html', variables=variables)


# Marketplace
@app.route('/marketplace', methods=['GET'])
def marketplace():
    # Python functions
    return render_template('marketplace.html',
                           interface=interface,
                           title="Marketplace")


# Profile
@app.route('/profile/<name>', methods=['GET'])
def profile(name):
    # Python functions
    return render_template('profile.html',
                           interface=interface,
                           title="Profile")


# Store
@app.route('/store/<name>', methods=['GET'])
def store(name):
    # Python functions
    if name in stores:
        return render_template('store.html',
                               interface=interface,
                               store=stores[name],
                               title="Store")
    else:
        # TODO redirect to 404 page
        return redirect(url_for('marketplace'))
