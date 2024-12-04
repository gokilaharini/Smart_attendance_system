import sqlite3
from werkzeug.security import generate_password_hash

def setup_database():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Create users table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        role TEXT NOT NULL
    )
    ''')
    
    # Insert sample users
    sample_users = [
        ('krishna', 'krishna@2006', 'employee'),
        ('gokila', 'gokila@2005', 'hr')
    ]
    
    for username, password, role in sample_users:
        password_hash = generate_password_hash(password)
        try:
            cursor.execute('''
            INSERT INTO users (username, password_hash, role)
            VALUES (?, ?, ?)
            ''', (username, password_hash, role))
        except sqlite3.IntegrityError:
            print(f"User {username} already exists")
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_database()