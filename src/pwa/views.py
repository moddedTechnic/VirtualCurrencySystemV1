'''
Views for the PWA app.
Mainly focuses on providing a function generator as PWA mostly serves static
files
'''

from typing import Any

from django.core.handlers.wsgi import WSGIRequest
from django.http.response import Http404, HttpResponse
from utils import serve

from . import settings


def manifest():
    manifest_data: dict[str, Any] = settings.MANIFEST_DATA
    if manifest_data['use_file']:
        return serve.static_file(manifest_data['filename'])

    if 'use_file' in manifest_data:
        del manifest_data['use_file']
    if 'filename' in manifest_data:
        del manifest_data['filename']

    return serve.json(manifest_data)


if settings.MANIFEST_FILE:
    manifest = serve.static_file('manifest.json')
else:
    def manifest(request: WSGIRequest) -> HttpResponse:  # pylint: disable=function-redefined
        raise Http404('Could not generate manifest')


__all__ = ['manifest']
