'''
Utilities related to loading files
'''

from pathlib import Path
from typing import Optional, Union

from django.conf import settings

from . import Result

class Error(Exception):
    'An error ocurred whilst loading a resource'


def static_file(
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
            return Result(ok=(data, fpath))
    return Result(err=f'Could not find {filename}')

__all__ = ['static_file']
