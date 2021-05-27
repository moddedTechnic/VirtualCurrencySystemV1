"""
Static files utils.

Includes:
- finding the path of a static item
"""

from pathlib import Path
from typing import Union

from main import settings

from . import Result


def path(filename: Union[str, Path]) -> Result[Path, FileNotFoundError]:
    if isinstance(filename, str):
        filename = filename.strip('/')
        if filename.startswith('static'):
            filename = filename[len('static'):]
        filename = filename.strip('/')
    for directory in settings.STATICFILES_DIRS:
        fpath: Path = directory / filename
        if fpath.exists():
            return Result(ok=fpath)
    result: Result[Path, str] = Result(err=f'File not found ({filename})')
    result.wrap_err(FileNotFoundError)
    return result


def mime_type(filename: Union[str, Path]) -> str:
    filename = Path(filename)
    suffix = filename.suffix[1:]
    return settings.MIME_TYPES.get(suffix, 'text/plain')


__all__ = ['path']
