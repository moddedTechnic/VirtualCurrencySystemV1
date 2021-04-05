'''
Utilities related to loading files
'''

from pathlib import Path
from typing import Optional, Union

from . import Result, static


class Error(Exception):
    'An error ocurred whilst loading a resource'


def static_file(
        filename: Union[str, Path],
        content_type: Optional[str] = None):
    try:
        data, fpath = static.path(filename).unwrap()
    except Exception as e: #pylint: disable=broad-except
        return Result(err=e)
    content_type = static.mime_type(fpath)
    return Result(ok=(data, fpath, content_type))

__all__ = ['static_file']
