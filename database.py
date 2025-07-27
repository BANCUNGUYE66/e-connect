import sqlite3

def init_db():
    conn = sqlite3.connect('data/econnect.db')
    c = conn.cursor()

    # Create tables
    c.execute('''CREATE TABLE IF NOT EXISTS graduates (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT UNIQUE,
        password TEXT
    )''')

    c.execute('''CREATE TABLE IF NOT EXISTS companies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT UNIQUE,
        password TEXT
    )''')

    c.execute('''CREATE TABLE IF NOT EXISTS jobs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        description TEXT,
        company_id INTEGER,
        FOREIGN KEY(company_id) REFERENCES companies(id)
    )''')

    c.execute('''CREATE TABLE IF NOT EXISTS applications (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        graduate_id INTEGER,
        job_id INTEGER,
        FOREIGN KEY(graduate_id) REFERENCES graduates(id),
        FOREIGN KEY(job_id) REFERENCES jobs(id)
    )''')

    conn.commit()
    conn.close()
