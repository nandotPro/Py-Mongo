from src.models.connection.connection_handler import db_connection_handler
from src.models.repository.orders_repository import OrdersRepository
from src.use_cases.get_order import GetOrder

def get_order_composer():
    db_connection = db_connection_handler.get_db_connection()
    model = OrdersRepository(db_connection)
    use_case = GetOrder(model)
    return use_case
