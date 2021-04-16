'''
Utilities related to loading files
'''

import json
from pathlib import Path
from typing import Optional, Union

from . import Result, static


class Error(Exception):
    'An error ocurred whilst loading a resource'


def static_file(
        filename: Union[str, Path],
        content_type: Optional[str] = None
) -> Result[tuple[str, Path, str], FileNotFoundError]:
    try:
        fpath: Path = static.path(filename).unwrap()
    except FileNotFoundError as e:
        return Result(err=e)
    content_type = static.mime_type(fpath)
    with fpath.open('rb') as f:
        data = f.read()
    return Result(ok=(data, fpath, content_type))

def json_file(filename: Union[str, Path]) -> Result[dict, FileNotFoundError]:
    if isinstance(filename, str):
        filename = filename.strip('/')
    path = Path(filename)

    if path.exists():
        with path.open('r') as f:
            return Result(ok=json.load(f))
    try:
        data, *_ = static_file(path).unwrap()
    except FileNotFoundError as e:
        return Result(err=e)
    return Result(ok=json.load(data))

__all__ = ['static_file', 'json_file']
