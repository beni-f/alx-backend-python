# Create a resuable context manager that takes a query as input and executes it, managing both connection and the query execution


import sqlite3

class ExecuteQuery:
    def __init__(self, query, parameter):
        self.query = query
        self.parameter = parameter
        self.conn = None

    def __enter__(self):
        self.conn = sqlite3.connect('user.db')
        cursor = self.conn.cursor()
        cursor.execute(f"{self.query}",(self.parameter,))
        return cursor.fetchall()
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.close()

with ExecuteQuery("SELECT * FROM users WHERE age > ?", 40) as result:
    print(result)
