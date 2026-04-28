#pip install mysql-connector-python
# OR 123.0.0.1
import mysql.connector
from mysql.connector import Error

config = {
    "host":'localhost',
    "user":"root",
    "password":"",
    "db":"python_test"
}
connection = None
try:
    connection = mysql.connector.connect(**config)
    if connection.is_connected():
        print("Connection Succesful :3 Wohooo")
        name = input("Please put your name in here: ")
        last_name = input("Please put your last name in here: ")
        email = input("Please put your EMAIL in here: ")
        password = input("Okay now your password punk: ")
        #Insert Data, Blah Blah Blah
        sql = "insert into users values (%s,%s,%s,%s,%s,%s)"
        values = (0,name,last_name,email,password,'default.jpg')
        cursor = connection.cursor()
        cursor.execute(sql,values)
        connection.commit()
        print("Registrado insertado correctamente")
        #Consultaaaaaar datos
        sql = "select * from users order by id_user DESC"
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            print("-"*50)
            print(f"Email: {row[3]}, Name: {row[1]}, Id: {row[0]}")
            print("-"*50)
except Error as e:
    print(f"ERROR: {e}")
finally:
    if connection and connection.is_connected():
        cursor.close()
        connection.close()