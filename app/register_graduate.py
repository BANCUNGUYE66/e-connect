import sqlite3

def register_graduate(name, email, password):
    conn = sqlite3.connect('data/econnect.db')
    c = conn.cursor()

    try:
        c.execute('INSERT INTO graduates (name, email, password) VALUES (?, ?, ?)', (name, email, password))
        conn.commit()
        print(f"✅ Graduate '{name}' registered successfully.")
    except sqlite3.IntegrityError:
        print("❌ Email already exists. Registration failed.")
    finally:
        conn.close()

if __name__ == "__main__":
    # Example usage:
    register_graduate("Alice Uwase", "alice@example.com", "123456")
