from abc import ABC, abstractmethod

class OrdersRepositoryInterface(ABC):
    @abstractmethod
    def insert_order(self, document: dict) -> None:
        pass

    @abstractmethod
    def insert_list_of_orders(self, documents: list[dict]) -> None:
        pass

    @abstractmethod
    def select_many_orders(self, document_filter: dict) -> list[dict]:
        pass

    @abstractmethod
    def select_one_order(self, document_filter: dict) -> dict:
        pass

    @abstractmethod
    def select_many_orders_with_properties(self, document_filter: dict) -> list[dict]:
        pass

    @abstractmethod
    def select_order_by_id(self, object_id: str) -> dict:
        pass

    @abstractmethod
    def update_order(self, object_id: str, document: dict) -> None:
        pass

    @abstractmethod
    def delete_order(self, object_id: str) -> None:
        pass
