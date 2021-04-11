'''All the middleware for the main module

Currently contains:
- `AddContextMiddleware`
'''

from typing import Any, Callable
from django.core.handlers.wsgi import WSGIRequest
from django.http.request import HttpRequest
from django.template.response import TemplateResponse

class AddContextMiddleware:
    'A mixin to add extra items to the context'

    def __init__(self, get_response: Callable[[WSGIRequest], Any]):
        print(f'Added middleware {self.__class__.__qualname__}')
        self.get_response = get_response

    def __call__(self, request: WSGIRequest) -> Any:
        response = self.get_response(request)
        return response

    def process_template_response(self,
        request: HttpRequest, response: TemplateResponse):
        response.context_data['request'] = request
        response.context_data['user'] = request.user
        return response
