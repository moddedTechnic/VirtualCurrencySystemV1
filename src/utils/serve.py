'''
Utilities related to serving files
'''

from json import dumps
from pathlib import Path
from typing import Any, Callable, Optional, Union

from django.conf import settings
from django.core.handlers.wsgi import WSGIRequest
from django.http.response import Http404, HttpResponse

class _Result:
    'Stores a result, either ok or error'
    def __init__(self, *, ok=None, err=None):
        self.ok = ok
        self.err = err

    def __bool__(self):
        return self.err is None

    def get(self):
        if self:
            return self.ok
        raise self.err

View = Callable[[WSGIRequest], HttpResponse]

def _load_static_file(
    filename: Union[str, Path],
    content_type: Optional[str] = None):
    for directory in settings.STATICFILES_DIRS:
        fpath: Path = directory / filename
        if fpath.exists():
            content_type = (
                content_type or {
                    'js': 'application/javascript',
                    'json': 'application/json',
                    'txt': 'text/plain',
                }.get(fpath.suffix[1:], 'text/plain')
            )
            with open(fpath, 'r') as f:
                data = f.read()
            return _Result(ok=HttpResponse(data, content_type=content_type))
    return _Result(err=Http404(f'Could not find {filename}'))

def static_file(
        filename: Union[str, Path],
        content_type: Optional[str] = None
    ) -> View:
    result = _load_static_file(filename, content_type)

    return lambda _: result.get()

def string(data: str, content_type: str = 'text/plain') -> View:
    return lambda _: HttpResponse(data, content_type=content_type)

def json(data: dict[str, Any]):
    return string(dumps(data), content_type='application/json')


__all__ = [ 'static_file', 'string', 'json' ]
