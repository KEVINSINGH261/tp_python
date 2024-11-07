
import uuid
from bookings_db import bookings_db

def get_all_bookings(offset=0, limit=10):
    bookings = list(bookings_db.values())[offset:offset + limit]
    return bookings

def get_booking(booking_id):
    return bookings_db.get(booking_id)

def create_booking(data):
    booking_id = str(uuid.uuid4())
    data["booking_id"] = booking_id
    bookings_db[booking_id] = data 
    return data


def update_booking(booking_id, data):
    if booking_id in bookings_db:
        data["booking_id"] = booking_id
        bookings_db[booking_id] = data
        return data
    return None

def delete_booking(booking_id):
    if booking_id in bookings_db:
        del bookings_db[booking_id]
        return True
    return False

def get_room_type_statistics():
    stats = {"SINGLE": 0, "DELUXE": 0, "SUITE": 0}
    for booking in bookings_db.values():
        if not booking["is_cancelled"]:
            stats[booking["room_type"]] += 1
    return stats
