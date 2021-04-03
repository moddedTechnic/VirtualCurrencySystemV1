'''
Views for the PWA app
Mainly focuses on providing a function generator as PWA mostly serves static files
'''

from pathlib import Path
from typing import Callable, Union

from django.conf import settings
from django.core.handlers.wsgi import WSGIRequest
from django.http.response import Http404, HttpResponse


def serve_static_file(
        filename: Union[str, Path],
        content_type: str = 'text/plain'
    ) -> Callable[[WSGIRequest], HttpResponse]:
    def wrapper(request: WSGIRequest) -> HttpResponse:
        del request  # unused
        for directory in settings.STATICFILES_DIRS:
            fpath: Path = directory / filename
            if fpath.exists():
                with open(fpath, 'r') as f:
                    return HttpResponse(f.read(), content_type=content_type)
        raise Http404(f'Could not find {filename}')
    return wrapper


__all__ = [ 'serve_static_file' ]
