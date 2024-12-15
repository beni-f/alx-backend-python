import sqlite3
import random
import string

def create_user_db():
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    """)

# Function to generate random user data
def generate_random_user():
    name = ''.join(random.choices(string.ascii_letters, k=8))  # Random 8-character name
    email = f"{name.lower()}@example.com"  # Random email based on the name
    return name, email

# Function to insert random users into the database
def insert_random_users(num_users):
    connection = sqlite3.connect('user.db')
    cursor = connection.cursor()

    for _ in range(num_users):
        name, email = generate_random_user()
        try:
            cursor.execute("INSERT INTO user (name, email) VALUES (?, ?)", (name, email))
        except sqlite3.IntegrityError:
            # Handle cases where email is not unique
            print(f"Failed to insert user with email: {email} (likely duplicate)")

    connection.commit()
    connection.close()
    print(f"{num_users} random users inserted successfully!")

if __name__ == "__main__":
    create_user_db()
    insert_random_users(10)
