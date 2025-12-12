from pyramid.httpexceptions import HTTPBadRequest
from pydantic import ValidationError as PydanticValidationError
from src.utils import AppError


def app_error_view(exc, request):
    request.response.status_code = exc.status_code
    return {"status": "error", "message": exc.message}


def register_error_handlers(config):
    config.add_view(app_error_view, context=AppError, renderer='json')
