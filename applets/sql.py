import pyodbc
from applets import app


conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                      'SERVER='+app.config['DB_SERVER_NAME'] +
                      ';DATABASE='+app.config['DB_DATABASE_NAME'] +
                      ';UID='+app.config['DB_USERNAME'] +
                      ';PWD='+app.config['DB_PASSWORD'])
cursor = conn.cursor()
cursor.execute("SELECT TOP 20 pc.Name as CategoryName, p.name as ProductName FROM [SalesLT].[ProductCategory] pc JOIN "
               "[SalesLT].[Product] p ON pc.productcategoryid = p.productcategoryid")
row = cursor.fetchone()
while row:
    print (str(row[0]) + " " + str(row[1]))
    row = cursor.fetchone()


