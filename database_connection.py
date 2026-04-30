import mysql.connector
from mysql.connector import Error

class Connection:
    def __init__(self):
        self.config = {
            "host":'localhost',
            "user":"root",
            "password":"",
            "db":"python_test"
        }
        self.connection = None
        self.cursor = None
    def connect(self):
        try:
            self.connection = mysql.connector.connect(**self.config)
            if self.connection.is_connected():
                print("Connection Succesful :3 Wohooo")
                self.cursor = self.connection.cursor()
        except Error as e:
            print(f"Error: {e}")
    #It goes for all inserting, modifying and eliminating data, just letting you know
    def insert(self, sql, values):
        self.cursor.execute(sql,values)
        self.connection.commit()
    def select(self, sql):
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        return results