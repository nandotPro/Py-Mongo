from flask import Blueprint, jsonify

orders_routes_bp = Blueprint("orders_routes", __name__)

@orders_routes_bp.route("/orders", methods=["POST"])
def create_order():
    return jsonify({"message": "Order created successfully"}), 201
