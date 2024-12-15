import sqlite3
class DatabaseConnection:
    def __init__(self):
        self.conn = None

    def __enter__(self):
        self.conn = sqlite3.connect('user.db')
        return self.conn
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.close()


with DatabaseConnection() as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()

print(result)

