from applets import app, sql
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
# @app.route('/product/<name>', methods=['GET'])
# def product(name):
#     # Python functions
#     images = ["img/marketplace/items/10.jpg", "img/marketplace/items/15.jpg", "img/marketplace/items/16.jpg", "img/marketplace/items/17.jpg", "img/marketplace/items/18.jpg", "img/marketplace/items/19.jpg"]
#     details = [
#         {"Allergens": "May contain nuts",
#          "Validity": "Consume in 10 days"}
#     ]
#     description = [
#         {"type": "title",
#          "value": "This is the title attracting factor"},
#         {"type": "text",
#          "value": "This product will be great hehe"},
#         {"type": "text",
#          "value": "This product will be great hehe"}
#     ]
#     inclusive = [
#         "Taadaa",
#         "Feature 2",
#         "Feature 10"
#     ]
#     return render_template('product.html',
#                            interface=interface,
#                            images=images,
#                            details=details,
#                            description=description,
#                            inclusive=inclusive,
#                            title="Product")

def split_detail(string):
    details = {}
    items = string.split(".")
    for item in items:
        [key, value] = item.split(',')
        details[key] = value
    return details


@app.route('/product/<id>', methods=['GET'])
def product(id):
    cur = sql.start_conn()
    product = sql.get_product(cur, id)
    if product:
        product['detail'] = split_detail(product['detail'])
        category = sql.get_category(cur, product['category_id'])
        images = sql.get_product_images(cur, id)
        store = sql.get_store(cur, product['maker_id'])

        # print(name)
        # filtered = list(filter(lambda item: str(item['id']) == id, items['items']))
        # print(filtered)
        return render_template('product.html',
                               interface=interface,
                               images=images,
                               store=store,
                               # item=filtered[0],
                               product=product,
                               category=category,
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

    return render_template('category.html',
                           interface=interface,
                           title="Category")
