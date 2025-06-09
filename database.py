import sqlite3
import pandas as pd

DB_NAME = "resources.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS resources (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    description TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS bookings (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_name TEXT,
                    resource_id INTEGER,
                    date TEXT,
                    status TEXT DEFAULT 'Pending',
                    FOREIGN KEY(resource_id) REFERENCES resources(id))''')
    conn.commit()
    conn.close()

def get_resources():
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql_query("SELECT * FROM resources", conn)
    conn.close()
    return df

def get_bookings():
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql_query("""
        SELECT b.id, b.user_name, r.name AS resource, b.date, b.status
        FROM bookings b
        JOIN resources r ON b.resource_id = r.id
        ORDER BY b.date DESC
    """, conn)
    conn.close()
    return df

def add_booking(user_name, resource_id, date):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO bookings (user_name, resource_id, date) VALUES (?, ?, ?)",
              (user_name, resource_id, date))
    conn.commit()
    conn.close()

def add_resource(name, description):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO resources (name, description) VALUES (?, ?)", (name, description))
    conn.commit()
    conn.close()

def update_booking_status(booking_id, new_status):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("UPDATE bookings SET status = ? WHERE id = ?", (new_status, booking_id))
    conn.commit()
    conn.close()