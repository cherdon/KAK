import pyodbc
from applets import app


def start_conn():
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                          'SERVER='+app.config['DB_SERVER_NAME'] +
                          ';DATABASE='+app.config['DB_DATABASE_NAME'] +
                          ';UID='+app.config['DB_USERNAME'] +
                          ';PWD='+app.config['DB_PASSWORD'])
    cursor = conn.cursor()
    return cursor


def get_product(cur, id):
    keys = ["id", "name", "price", "size", "detail", "description", "category_id", "maker_id"]
    product = {}
    cur.execute("SELECT * FROM [dbo].[product] WHERE id = {}".format(id))
    row = cur.fetchone()
    while row:
        for i in range(len(row)):
            product[keys[i]] = row[i]
        row = cur.fetchone()
    return product


def get_store(cur, id):
    keys = ["id", "name", "image", "username", "follower_count", "verification", "about", "item_count", "review_count", "avatar", "flag", "flagname"]
    store = {}
    cur.execute("SELECT * FROM [dbo].[store] WHERE id = {}".format(id))
    row = cur.fetchone()
    while row:
        for i in range(len(row)):
            store[keys[i]] = row[i]
        row = cur.fetchone()
    return store


def get_category(cur, id):
    keys = ["id", "name"]
    category = {}
    cur.execute("SELECT * FROM [dbo].[category] WHERE id = {}".format(id))
    row = cur.fetchone()
    while row:
        for i in range(len(row)):
            category[keys[i]] = row[i]
        row = cur.fetchone()
    return category


def get_product_images(cur, id):
    images = []
    cur.execute("SELECT * FROM [dbo].[map_product_image] WHERE product_id = {}".format(id))
    row = cur.fetchone()
    while row:
        images.append(row[1])
        row = cur.fetchone()
    return images


conn = start_conn()
product = get_product_images(conn, 1)
print(product)

# cursor.execute("SELECT TOP (1000) * FROM [dbo].[map_product_image]")
# row = cursor.fetchone()
# while row:
#     print(row)
#     # print(str(row[0]) + " " + str(row[1]))
#     row = cursor.fetchone()


