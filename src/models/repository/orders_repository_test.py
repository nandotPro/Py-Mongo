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

@pytest.mark.skip(reason="integration test")
def test_select_many_orders():
    orders_repository = OrdersRepository(connection)
    orders = orders_repository.select_many_orders({"cupom": False})
    print(orders)

@pytest.mark.skip(reason="integration test")
def test_select_one_order():
    orders_repository = OrdersRepository(connection)
    order = orders_repository.select_one_order({"cupom": False})
    print(order)

@pytest.mark.skip(reason="integration test")
def test_select_many_orders_with_properties():
    orders_repository = OrdersRepository(connection)
    orders = orders_repository.select_many_orders_with_properties({"cupom": False})
    print(orders)

@pytest.mark.skip(reason="integration test")
def test_select_order_by_id():
    orders_repository = OrdersRepository(connection)
    order = orders_repository.select_order_by_id("669955778899001122334455")
    print(order)

@pytest.mark.skip(reason="integration test")
def test_update_order():
    orders_repository = OrdersRepository(connection)
    orders_repository.update_order("669955778899001122334455", {"name": "Test Order Updated"})

@pytest.mark.skip(reason="integration test")
def test_delete_order():
    orders_repository = OrdersRepository(connection)
    orders_repository.delete_order("669955778899001122334455")
