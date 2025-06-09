def format_booking(booking):
    booking_id, user_name, resource_name, timestamp, status = booking
    return f"📌 Booking #{booking_id} by {user_name} for '{resource_name}' on {timestamp} — Status: {status}"
