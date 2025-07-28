import sqlite3
import os

def show_tables():
    # Calculate absolute path to DB file
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    db_path = os.path.join(BASE_DIR, 'data', 'econnect.db')
    
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = c.fetchall()
    
    if tables:
        print("📋 Tables in the database:")
        for table in tables:
            print(f"- {table[0]}")
    else:
        print("⚠️ No tables found in the database.")
    
    conn.close()
