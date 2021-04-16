'''All the middleware for the PWA module

Currently contains:
- `PWASettingsMiddleware`
'''

from typing import Any, Callable
from django.core.handlers.wsgi import WSGIRequest
from django.http.request import HttpRequest
from django.template.response import TemplateResponse
from . import settings


class PWASettingsMiddleware:
    'A mixin to add appropriate PWA settings to the context'

    def __init__(self, get_response: Callable[[WSGIRequest], Any]):
        print(f'Added middleware {self.__class__.__qualname__}')
        self.get_response = get_response

    def __call__(self, request: WSGIRequest) -> Any:
        response = self.get_response(request)
        return response

    def process_template_response(self,
        request: HttpRequest, response: TemplateResponse):
        del request  # unuser
        response.context_data['load_service_worker'] = \
            settings.LOAD_SERVICE_WORKER
        return response
