'''
Utilities related to serving files
'''

from json import dumps
from pathlib import Path
from typing import Any, Callable, Optional, Union

from django.core.handlers.wsgi import WSGIRequest
from django.http.response import Http404, HttpResponse

from . import load, static

View = Callable[[WSGIRequest], HttpResponse]

def static_file(
        filename: Union[str, Path],
        content_type: Optional[str] = None
    ) -> View:
    result = load.static_file(filename, content_type)
    result.wrap_err(Http404)
    result, fpath = result.unwrap()
    content_type = content_type or static.mime_type(fpath)
    result = HttpResponse(result, content_type=content_type)
    return lambda _: result

def string(data: str, content_type: str = 'text/plain') -> View:
    return lambda _: HttpResponse(data, content_type=content_type)

def json(data: dict[str, Any]):
    return string(dumps(data), content_type='application/json')


__all__ = [ 'static_file', 'string', 'json' ]
