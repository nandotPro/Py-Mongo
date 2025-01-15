from flask import Blueprint, request
from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse

orders_routes_bp = Blueprint("orders_routes", __name__)

@orders_routes_bp.route("/orders", methods=["POST"])
def create_order():
    http_request = HttpRequest(body=request.json)
    http_response = HttpResponse(status_code=201, body={"message": "Order created successfully"})
    return http_response
