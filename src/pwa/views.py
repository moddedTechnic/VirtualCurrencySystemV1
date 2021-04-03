'''
Views for the PWA app.
Mainly focuses on providing a function generator as PWA mostly serves static
files
'''

from typing import Any

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


__all__ = ['manifest']
