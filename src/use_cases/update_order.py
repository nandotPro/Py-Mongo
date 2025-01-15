from src.models.repository.interfaces.orders_repository_interface import OrdersRepositoryInterface
from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse
from src.errors.errors_types.http_not_found_error import HttpNotFoundError
from src.errors.error_handler import handle_error
from src.validators.create_order_validator import validate_create_order

class UpdateOrder:
    def __init__(self, orders_repository: OrdersRepositoryInterface) -> None:
        self.__orders_repository = orders_repository

    def execute(self, http_request: HttpRequest) -> HttpResponse:
        try:
            order_id = http_request.path_params["order_id"]
            body = http_request.body
            self.__search_order(order_id)
            self.__validate_body(body)
            formatted_order = self.__format_order(body)
            self.__update_order(order_id, formatted_order)
            updated_order = self.__search_order(order_id)
            return self.__format_response(updated_order)
        except Exception as e:
            return handle_error(e)

    def __search_order(self, order_id: str) -> dict:
        order = self.__orders_repository.select_order_by_id(order_id)
        if not order:
            raise HttpNotFoundError("Order not found")
        return order

    def __validate_body(self, body: dict) -> None:
        validate_create_order(body)

    def __format_order(self, body: dict) -> dict:
        return body["data"]

    def __update_order(self, order_id: str, order: dict) -> None:
        self.__orders_repository.update_order(order_id, order)

    def __format_response(self, order: dict) -> HttpResponse:
        return HttpResponse(status_code=200, body={"data": order})
