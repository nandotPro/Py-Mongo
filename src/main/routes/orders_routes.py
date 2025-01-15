from flask import Blueprint, request, jsonify
from src.main.http_types.http_request import HttpRequest
from src.main.composer.create_order_composer import create_order_composer
from src.main.composer.get_order_composer import get_order_composer
from src.main.composer.update_order_composer import update_order_composer


orders_routes_bp = Blueprint("orders_routes", __name__)

@orders_routes_bp.route("/orders", methods=["POST"])
def create_order():
    http_request = HttpRequest(body=request.json)
    use_case = create_order_composer()
    response = use_case.execute(http_request)
    return jsonify(response.body), response.status_code

@orders_routes_bp.route("/orders/<order_id>", methods=["GET"])
def get_order(order_id: str):
    http_request = HttpRequest(path_params={"order_id": order_id})
    use_case = get_order_composer()
    response = use_case.execute(http_request)
    return jsonify(response.body), response.status_code

@orders_routes_bp.route("/orders/<order_id>", methods=["PUT"])
def update_order(order_id: str):
    http_request = HttpRequest(path_params={"order_id": order_id}, body=request.json)
    use_case = update_order_composer()
    response = use_case.execute(http_request)
    return jsonify(response.body), response.status_code
