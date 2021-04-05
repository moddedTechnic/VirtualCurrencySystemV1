'''
Static files utils.

Includes:
- finding the path of a static item
'''

from pathlib import Path
from typing import Union

from django.conf import settings

from . import Result


def path(filename: Union[str, Path]) -> Result:
    if isinstance(filename, str):
        filename = filename.strip('/')
    for directory in settings.STATICFILES_DIRS:
        fpath: Path = directory / filename
        if fpath.exists():
            return Result(ok=fpath)
    result = Result(err=f'File not found ({filename})')
    result.wrap_err(FileNotFoundError)
    return result

def mime_type(filename: Union[str, Path]) -> str:
    filename = Path(filename)
    suffix = filename.suffix[1:]
    return {
        'js': 'application/javascript',
        'json': 'application/json',
        'css': 'text/css',
        'html': 'text/html',
        'txt': 'text/plain',
    }.get(suffix, 'text/plain')

__all__ = ['path']
