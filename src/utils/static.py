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
    for directory in settings.STATICFILES_DIRS:
        fpath: Path = directory / filename
        if fpath.exists():
            return Result(ok=fpath)
    result = Result(err=f'File not found ({filename})')
    result.wrap_err(FileNotFoundError)
    return result

__all__ = ['path']
