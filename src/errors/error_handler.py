from src.errors.errors_types.http_not_found_error import HttpNotFoundError
from src.errors.errors_types.http_bad_request_error import HttpBadRequestError
from src.errors.errors_types.http_unprocessable_entity_error import HttpUnprocessableEntityError
from src.main.http_types.http_response import HttpResponse

def handle_error(error: Exception) -> HttpResponse:
    if isinstance(error, (HttpNotFoundError, HttpBadRequestError, HttpUnprocessableEntityError)):
        return HttpResponse(error.status_code, body={
            "title": error.error_type, 
            "detail": error.message,
        })
    return HttpResponse(500, body={
        "title": "internal_server_error", 
        "detail": str(error),
    })
