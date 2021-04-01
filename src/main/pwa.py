'''
Create urls and views to fulfill PWA requirements and similar

Adds:
- manifest.json
- robots.txt
'''

from pathlib import Path
from typing import Callable, Union

from django.urls import path
from django.core.handlers.wsgi import WSGIRequest
from django.http.response import Http404, HttpResponse
from django.conf import settings


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


app_name = 'pwa'

urlpatterns = [
    path('manifest.json', serve_static_file('manifest.json')),
    path('manifest', serve_static_file('manifest.json')),
    path('robots.txt', serve_static_file('robots.txt')),
    path('robots', serve_static_file('robots.txt')),
]
