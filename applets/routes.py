from applets import app
from flask import request, render_template, redirect, url_for, flash
interface = app.config['INTERFACE']
stores = app.config['STOREDB']
items = app.config['ITEMSDB']


# # HOME PAGE
# @app.route('/', methods=['GET'])
# def index():
#     # Example parameters
#     # This is where your functions from python come from
#     variables = ['This is variable one', 'This is variable two']
#     return render_template('index.html', variables=variables)


# 404 Not Found
@app.route('/404', methods=['GET'])
def error():
    # Python functions
    return render_template('404.html',
                           interface=interface,
                           title="Not Found")


# Login
@app.route('/login', methods=['GET'])
def login():
    # Python functions
    return render_template('login.html',
                           interface=interface,
                           title="Login")


# Marketplace
@app.route('/marketplace', methods=['GET'])
def marketplace():
    # Python functions
    return render_template('marketplace.html',
                           interface=interface,
                           items=items['items'],
                           store=stores,
                           title="Marketplace")


# Profile
@app.route('/profile/<name>', methods=['GET'])
def profile(name):
    # Python functions
    return render_template('profile.html',
                           interface=interface,
                           title="Profile")


# About
@app.route('/about', methods=['GET'])
def about():
    # Python functions
    return render_template('about.html',
                           interface=interface,
                           title="About")


# Store
@app.route('/store/<name>', methods=['GET'])
def store(name):
    # Python functions
    if name in stores:
        filtered = list(filter(lambda item: str(item['shop_id']) == name, items['items']))
        return render_template('store.html',
                               interface=interface,
                               store=stores[name],
                               items=filtered,
                               title="Store")
    else:
        return redirect(url_for('error'))


# Product
@app.route('/product/<name>', methods=['GET'])
def product(name):
    # Python functions
    inclusive = [
        "Products made with love, provided by KAKtus!"
    ]

    filtered = list(filter(lambda item: str(item['id']) == name, items['items']))
    if filtered:
        return render_template('product.html',
                               interface=interface,
                               item=filtered[0],
                               inclusive=inclusive,
                               title="Product")

    else:
        return redirect(url_for('error'))


# Forum
@app.route('/forum', methods=['GET'])
def forum():
    # Python functions
    return render_template('forum.html',
                           interface=interface,
                           title="Forum")


# Category
@app.route('/category/<name>', methods=['GET'])
def category(name):
    # Python functions
    filtered = list(filter(lambda item: str(item['cat']) == name, items['items']))
    return render_template('category.html',
                           interface=interface,
                           items=filtered,
                           store=stores,
                           title="Category")
