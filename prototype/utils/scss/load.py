
from typing import Union
from pathlib import Path


def file(fpath: Union[str, Path]) -> str:
    fpath = Path(fpath)
    with fpath.open('r') as f:
        data = f.read()
    return data
