from datetime import datetime
from src.models.repository.interfaces.orders_repository_interface import OrdersRepositoryInterface
from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse


class CreateOrder:
    def __init__(self, orders_repository: OrdersRepositoryInterface) -> None:
        self.__orders_repository = orders_repository

    def execute(self, http_request: HttpRequest) -> HttpResponse:
        try:
            body = http_request.body
            formatted_order = self.__format_order(body)
            self.__register_order(formatted_order)
            return self.__format_response()
        except Exception as e:
            return HttpResponse(status_code=400, body={"message": str(e)})

    def __format_order(self, body: dict) -> dict:
        new_order = body["data"]
        new_order = { **new_order, "created_at": datetime.now() }
        return new_order

    def __register_order(self, order: dict) -> None:
        self.__orders_repository.insert_order(order)

    def __format_response(self) -> dict:
        return HttpResponse(status_code=201, body={"message": "Order created successfully"})
