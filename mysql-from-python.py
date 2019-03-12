import os
import pymysql

#Get username from Cloud9 workspace

username = os.getenv('C9_USER')

#Connect to the database

connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='',)
                            
try:
    # Run a query
    with connection.cursor() as cursor: 
        sql = "SELECT * FROM Recipes;"
        cursor.execture.(sql)
        result = cursos.fetchall()
        print(result)
finally:
    # Close connection
    connection.close()