# app/controller/booking_controller.py

from flask import Blueprint, jsonify, request
from flask_expects_json import expects_json
from service.booking_service import (
    get_all_bookings, get_booking, create_booking, update_booking, delete_booking, get_room_type_statistics
)
from schema.booking_schema import booking_schema

booking_bp = Blueprint("booking", __name__)

@booking_bp.route("/bookings", methods=["GET"])
def get_bookings():
    offset = int(request.args.get("offset", 0))
    limit = int(request.args.get("limit", 10))
    bookings = get_all_bookings(offset, limit)
    return jsonify(bookings), 200

@booking_bp.route("/bookings/<string:booking_id>", methods=["GET"])
def get_single_booking(booking_id):
    booking = get_booking(booking_id)
    if booking:
        return jsonify(booking), 200
    return jsonify({"error": "Booking not found"}), 404

@booking_bp.route("/bookings", methods=["POST"])
@expects_json(booking_schema)
def create_new_booking():
    data = request.get_json()
    new_booking = create_booking(data)
    return jsonify(new_booking), 201

@booking_bp.route("/bookings/<string:booking_id>", methods=["PUT"])
@expects_json(booking_schema)
def update_existing_booking(booking_id):
    data = request.get_json()
    updated_booking = update_booking(booking_id, data)
    if updated_booking:
        return jsonify(updated_booking), 200
    return jsonify({"error": "Booking not found"}), 404

@booking_bp.route("/bookings/<string:booking_id>", methods=["DELETE"])
def delete_existing_booking(booking_id):
    if delete_booking(booking_id):
        return "", 204
    return jsonify({"error": "Booking not found"}), 404

@booking_bp.route("/statistics/room_type", methods=["GET"])
def get_room_type_stats():
    stats = get_room_type_statistics()
    return jsonify(stats), 200
