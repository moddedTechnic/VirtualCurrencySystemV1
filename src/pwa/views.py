'''
Views for the PWA app.
Mainly focuses on providing a function generator as PWA mostly serves static
files
'''

import json
from pathlib import Path
from typing import Any, Union

from utils import Result, serve, static

from . import settings


def _strip_keys(d: dict, *keys):
    for key in keys:
        if key in d:
            del d[key]
    return d


_directory_indices = {'index.json'}
def _get_icon_file(icons_path: Union[str, Path]):
    if isinstance(icons_path, str):
        icons_path = icons_path.strip('/')

    try:
        path: Path = static.path(icons_path).unwrap()
        if path.is_file():
            return Result(ok=path)
    except FileNotFoundError:
        pass
    for index in _directory_indices:
        try:
            return Result(ok=static.path(Path(icons_path) / index).unwrap())
        except FileNotFoundError:
            pass
    return Result(
        err=f'Could not find file ({icons_path})').wrap_err(FileNotFoundError)


def manifest():
    manifest_data: dict[str, Any] = settings.MANIFEST_DATA.copy()
    if manifest_data['use_file']:
        return serve.static_file(manifest_data['filename'])

    if not manifest_data['icons'] and manifest_data.get('icons_path', False):
        try:
            icons_path = _get_icon_file(manifest_data['icons_path']).unwrap()
        except FileNotFoundError as e:
            print('Error loading manifest:', e)
        else:
            suffix = icons_path.suffix
            if suffix == '.json':
                with open(icons_path, 'r') as f:
                    manifest_data['icons'] = json.load(f)
            else:
                print(f'Error loading manifest: Unknown icon path suffix ({suffix})')

    manifest_data = _strip_keys(
        manifest_data, 'use_file', 'filename', 'icons_path')

    return serve.json(manifest_data)


__all__ = ['manifest']
