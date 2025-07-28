import sqlite3

def show_graduates():
    conn = sqlite3.connect('data/econnect.db')
    c = conn.cursor()

    c.execute('SELECT id, name, email FROM graduates')
    rows = c.fetchall()

    print("\n👩‍🎓 Registered Graduates:")
    if not rows:
        print("No graduates found.")
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}")

    conn.close()

if __name__ == "__main__":
    show_graduates()
