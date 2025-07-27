import sqlite3
import getpass

DB_PATH = 'data/econnect.db'

def register_graduate():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = getpass.getpass("Enter your password: ")

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    try:
        c.execute("INSERT INTO graduates (name, email, password) VALUES (?, ?, ?)", (name, email, password))
        conn.commit()
        print("Registration successful!")
    except sqlite3.IntegrityError:
        print("Error: Email already exists.")
    finally:
        conn.close()

def login_graduate():
    email = input("Enter your email: ")
    password = getpass.getpass("Enter your password: ")

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM graduates WHERE email = ? AND password = ?", (email, password))
    user = c.fetchone()
    conn.close()

    if user:
        print(f"Welcome back, {user[1]}!")
        # You can add logic here to display graduate options
    else:
        print("Login failed. Please check your credentials.")