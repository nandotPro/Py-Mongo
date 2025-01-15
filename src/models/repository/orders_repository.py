from src.models.connection.connection_handler import DBConnectionHandler

class OrdersRepository:
    def __init__(self, db_connection: DBConnectionHandler) -> None:
        self.__collection_name = "orders"
        self.__db_connection = db_connection

    def insert_order(self, document: dict) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_one(document)

    def insert_list_of_orders(self, documents: list[dict]) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_many(documents)

    def select_many_orders(self, document_filter: dict) -> list[dict]:
        collection = self.__db_connection.get_collection(self.__collection_name)
        return collection.find(document_filter)

    def select_one_order(self, document_filter: dict) -> dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        return collection.find_one(document_filter)

    def select_many_orders_with_properties(self, document_filter: dict) -> list[dict]:
        collection = self.__db_connection.get_collection(self.__collection_name)
        return collection.find(document_filter, {"name": 1, "price": 1})

