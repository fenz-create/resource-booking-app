import sqlite3

conn = sqlite3.connect("data.db", check_same_thread=False)
c = conn.cursor()

def get_all_resources():
    c.execute("SELECT * FROM resources")
    return c.fetchall()

def get_all_bookings():
    c.execute("SELECT bookings.id, bookings.user_name, resources.name, bookings.timestamp, bookings.status FROM bookings JOIN resources ON bookings.resource_id = resources.id")
    return c.fetchall()

def add_booking(user_name, resource_id):
    c.execute("INSERT INTO bookings (user_name, resource_id, status) VALUES (?, ?, 'Pending')", (user_name, resource_id))
    conn.commit()

def update_booking_status(booking_id, status):
    c.execute("UPDATE bookings SET status = ? WHERE id = ?", (status, booking_id))
    conn.commit()

def add_resource(name):
    c.execute("INSERT INTO resources (name) VALUES (?)", (name,))
    conn.commit()
