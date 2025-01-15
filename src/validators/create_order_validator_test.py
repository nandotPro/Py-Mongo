import pytest
from src.validators.create_order_validator import validate_create_order

def test_validate_create_order():
    body = {
        "data": {
            "name": "John Doe",
            "address": "123 Main St, Anytown, USA",
            "cupom": True,
            "items": [
                { "item": "item1", "quantity": 1 },
                { "item": "item2", "quantity": 2 },
            ]
        }
    }
    validate_create_order(body)

def test_validate_create_order_invalid_body():
    body = {
        "data": {
            "name": "John Doe",
            "address": "123 Main St, Anytown, USA",
            "cupom": "error",
            "items": [
                { "item": "item1", "quantity": 1 },
                { "item": "item2", "quantity": 2 },
            ]
        }
    }
    with pytest.raises(Exception):
        validate_create_order(body)
