'''
Views for the PWA app.

Provides:
- manifest generator
'''

from pathlib import Path
from typing import Any, Union

from utils import Result, serve, static, load

from . import settings


def _strip_keys(d: dict, *keys):
    for key in keys:
        if key in d:
            del d[key]
    return d


_directory_indices = {'index.json'}


def _get_index_file(index_path: Union[str, Path]
                    ) -> Result[Path, FileNotFoundError]:
    if isinstance(index_path, str):
        index_path = index_path.strip('/')

    try:
        path: Path = static.path(index_path).unwrap()
        if path.is_file():
            return Result(ok=path)
    except FileNotFoundError:
        pass
    for index in _directory_indices:
        try:
            return Result(ok=static.path(Path(index_path) / index).unwrap())
        except FileNotFoundError:
            pass
    return Result(
        err=f'Could not find file ({index_path})').wrap_err(FileNotFoundError)

def _load_array(manifest_data, arr_name, processor=None):
    if (not manifest_data[arr_name] and
        manifest_data.get(f'{arr_name}_path', False)):
        try:
            icons_path = _get_index_file(manifest_data[f'{arr_name}_path'])
            icons_path = icons_path.unwrap()
        except FileNotFoundError as e:
            print('Error loading manifest:', e)
        else:
            suffix = icons_path.suffix
            if suffix == '.json':
                items = load.json_file(icons_path).unwrap()
                if processor:
                    manifest_data[arr_name] = [
                        processor(item) for item in items]
                else:
                    manifest_data[arr_name] = items
            else:
                print(
                    'Error loading manifest:'
                    f' Unknown {arr_name} path suffix ({suffix})'
                )
    return manifest_data


def manifest():
    manifest_data: dict[str, Any] = settings.MANIFEST_DATA.copy()
    if manifest_data['use_file']:
        return serve.static_file(manifest_data['filename'])

    def processor(item):
        if 'type' not in item:
            item['type'] = static.mime_type(item['src'])
        return item


    manifest_data = _load_array(manifest_data, 'icons', processor=processor)
    manifest_data = _load_array(
        manifest_data, 'screenshots', processor=processor)

    manifest_data = _strip_keys(
        manifest_data, 'use_file', 'filename', 'icons_path', 'screenshots_path')

    return serve.json(manifest_data)


__all__ = ['manifest']
