import pytest
from src.models.connection.connection_handler import DBConnectionHandler
from src.models.repository.orders_repository import OrdersRepository

db_connection = DBConnectionHandler()
db_connection.connect_to_db()
connection = db_connection.get_db_connection()

@pytest.mark.skip(reason="integration test")
def test_insert_order():
    orders_repository = OrdersRepository(connection)
    orders_repository.insert_order({"name": "Test Order", "price": 100})

@pytest.mark.skip(reason="integration test")
def test_insert_list_of_orders():
    orders_repository = OrdersRepository(connection)
    orders_repository.insert_list_of_orders(
        [
            {"name": "Test Order", "price": 100},
            {"name": "Test Order 2", "price": 200},
        ]
    )
