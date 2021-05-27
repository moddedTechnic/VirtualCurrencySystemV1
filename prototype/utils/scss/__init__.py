from pathlib import Path
from typing import Any
from utils.scss.tokens import TokenType

log_file = Path(__file__).parent / 'log.txt'
with log_file.open('w') as f:
    f.write('')


def log(*msg: Any, sep: str = ' ', end: str = '\n'):
    with log_file.open('a') as f:
        f.write(sep.join(str(m) for m in msg) + end)


def compile(source: Path):
    from .lexer import Lexer
    from .parser import Parser
    with source.open('r') as f:
        data = f.read()
    tokens = Lexer(data)()
    ast = Parser(tokens)()
    list(ast)
    # print(list(tokens))
