import csv
import mysql.connector
from mysql.connector import Error
from config import Config
import uuid

def connect_db():
    try:
        print("Trying...")
        connection = mysql.connector.connect(
            host="localhost",
            user="airbnb_sys",
            password=Config.PASSWORD,
        )
        return connection
    except Error as e:
        print(e)
        return None
    
def create_database(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
    except Error as e:
        print(e)
    finally:
        cursor.close()

def connect_to_prodev():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='airbnb_sys',
            password=Config.PASSWORD,
            database='ALX_prodev',
        )
        return connection
    except Error as e:
        print(e)
        return None

def create_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_data (
                user_id CHAR(36) PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL UNIQUE,
                age DECIMAL(5, 2) NOT NULL
            );
        """)
    except Error as e:
        print(e)
    finally:
        cursor.close()

def insert_data(connection, data):
    try:
        cursor = connection.cursor()
        with open(data, 'r') as file:
            reader = csv.DictReader(file)
            print(reader)
            for row in reader:
                user_id = str(uuid.uuid4())
                insert_query = """
                    INSERT INTO user_data (user_id, name, email, age) VALUES (%s, %s, %s, %s)
                    ON DUPLICATE KEY UPDATE email=email;
                """
                cursor.execute(insert_query, (user_id, row['name'], row['email'], row['age']))
        connection.commit()
    except Error as e:
        print(e)
    finally:
        cursor.close()
