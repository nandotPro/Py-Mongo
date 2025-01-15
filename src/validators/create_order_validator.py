from cerberus import Validator

def validate_create_order(body: any):
    body_schema = Validator({
        "data": {
            "type": "dict",
            "schema": {
                "name": {"type": "string", "required": True},
                "address": {"type": "string", "required": True},
                "cupom": {"type": "boolean", "required": True},
                "items": {
                    "type": "list",
                    "required": True,
                    "schema": {
                        "type": "dict",
                        "schema": {
                            "item": {"type": "string", "required": True},
                            "quantity": {"type": "integer", "required": True}
                        }
                    }
                }
            }
        }
    })

    response = body_schema.validate(body)
    if response is False:
        raise Exception(body_schema.errors)
    
    return response
