from flask import Blueprint, request, jsonify
from src.main.http_types.http_request import HttpRequest
from src.main.composer.create_order_composer import create_order_composer

orders_routes_bp = Blueprint("orders_routes", __name__)

@orders_routes_bp.route("/orders", methods=["POST"])
def create_order():
    http_request = HttpRequest(body=request.json)
    use_case = create_order_composer()
    response = use_case.execute(http_request)
    return jsonify(response.body), response.status_code
