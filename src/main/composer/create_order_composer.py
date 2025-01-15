from src.models.connection.connection_handler import db_connection_handler
from src.models.repository.orders_repository import OrdersRepository
from src.use_cases.create_order import CreateOrder

def create_order_composer():
    db_connection = db_connection_handler.get_db_connection()
    model = OrdersRepository(db_connection)
    use_case = CreateOrder(model)
    return use_case
