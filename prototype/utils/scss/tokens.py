from enum import Enum
from dataclasses import dataclass
from typing import Any


def idx():
    idx.id += 1
    return idx.id


idx.id = -1


class TokenType(Enum):
    UNKNOWN = idx()

    NAME = idx()
    NUMBER = idx()
    WHITESPACE = idx()

    LPAREN = '('
    RPAREN = ')'
    LBRACE = '{'
    RBRACE = '}'
    LSQBRAC = '['
    RSQBRAC = ']'

    COMMA = ','
    PERIOD = '.'
    COLON = ':'
    SEMICOLON = ';'
    DOLLAR = '$'
    AT = '@'

    DASH = '-'
    STAR = '*'

    @classmethod
    def from_char(cls, char: str, default=None):
        for k in dir(cls):
            if k.isupper():
                token_type: TokenType = getattr(cls, k)
                if token_type.value == char:
                    return token_type
        return cls.UNKNOWN if default is None else default


@dataclass
class Token:
    type: TokenType
    value: Any
