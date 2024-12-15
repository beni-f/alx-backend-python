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
            email TEXT NOT NULL UNIQUE,
            age INTEGER NOT_NULL
        )
    """)

# Function to generate random user data
def generate_random_user():
    name = ''.join(random.choices(string.ascii_letters, k=8))  # Random 8-character name
    email = f"{name.lower()}@example.com"  # Random email based on the name
    age = random.randint(18, 80)
    return name, email, age

# Function to insert random users into the database
def insert_random_users(num_users):
    connection = sqlite3.connect('user.db')
    cursor = connection.cursor()

    for _ in range(num_users):
        name, email, age = generate_random_user()
        try:
            cursor.execute("INSERT INTO user (name, email, age) VALUES (?, ?, ?)", (name, email, age))
        except sqlite3.IntegrityError:
            # Handle cases where email is not unique
            print(f"Failed to insert user with email: {email} (likely duplicate)")

    connection.commit()
    connection.close()
    print(f"{num_users} random users inserted successfully!")

if __name__ == "__main__":
    create_user_db()
    insert_random_users(10)
