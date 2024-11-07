booking_schema = {
    "type": "object",
    "properties": {
        "user_id": {"type": "string"},
        "start_date": {"type": "string"},
        "end_date": {"type": "string"},
        "is_cancelled": {"type": "boolean"},
        "is_paid": {"type": "boolean"},
        "price": {"type": "number", "minimum": 0},
        "room_type": {"type": "string", "enum": ["SINGLE", "DELUXE", "SUITE"]}
    },
    "required": ["user_id", "start_date", "end_date", "is_cancelled", "is_paid", "price", "room_type"],
    "additionalProperties": False
}