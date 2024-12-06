# Create a decorator that logs database queries executed by any function

import sqlite3
import functools

def log_queries(orig_func):
    import logging
    logging.basicConfig(filename='users.log', level=logging.INFO)
    @functools.wraps(orig_func)
    def wrapper(*args, **kwargs):
        query = args[0]
        result = orig_func(*args, **kwargs)
        logging.info(f"Executing Query: {query}")
        logging.info(f"Query result: {result}")
        return result
    return wrapper


@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")