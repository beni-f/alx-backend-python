# Create a resuable context manager that takes a query as input and executes it, managing connection and the query execution

import sqlite3
class ExectueQuery:
    def __init__(self, query, parameter):
        self.query = query
        self.parameter = parameter
        self.conn = None

    def __enter__(self):
        self.conn = sqlite3.connect('users.db')
        cursor = self.conn.cursor()
        cursor.execute(self.query)
        return cursor.fetchall()

    def __exit__(self):
        self.conn.close()

with ExectueQuery('SELECT * FROM users WHERE age > 25') as query:
    print(query)
