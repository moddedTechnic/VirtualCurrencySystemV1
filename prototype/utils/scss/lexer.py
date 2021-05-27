
from typing import Iterable, Optional

from . import log
from .tokens import Token, TokenType

WHITESPACE = set(' \n\r\t')
LETTERS = 'abcdefghijklmnopqrstuvwxyz'
LETTERS += LETTERS.upper()
LETTERS = set(LETTERS)
NUMBER = set('0123456789.')


class Lexer:
    def __init__(self, data: Iterable[str]):
        self.data = iter(data)
        self.current_char: Optional[str] = None

    def __iter__(self):
        yield next(self)
        while next(self) is not None:
            yield self.current_char

    def __next__(self):
        try:
            self.current_char = next(self.data)
        except StopIteration:
            self.current_char = None
        return self.current_char

    def __call__(self, data: Optional[Iterable[str]] = None):
        if data is not None:
            self.data = iter(data)

        for char in self:
            if char in WHITESPACE:
                yield Token(TokenType.WHITESPACE, char)
            elif char in LETTERS:
                yield Token(TokenType.NAME, self.generate_name())
                yield Token(TokenType.from_char(char), self.current_char)
            elif char in NUMBER:
                yield Token(TokenType.NAME, self.generate_name())
                yield Token(TokenType.from_char(char), self.current_char)
            else:
                log(Token(TokenType.from_char(char), char))
                yield Token(TokenType.from_char(char), char)

    def visit(self):
        if self.current_char in WHITESPACE:
            return Token(TokenType.WHITESPACE, self.current_char),
        if self.current_char in LETTERS:
            return Token(TokenType.NAME, self.generate_name()), *self.visit()
        if self.current_char in NUMBER:
            return Token(TokenType.NAME, self.generate_number()), *self.visit()
        return Token(TokenType.from_char(self.current_char), self.current_char)

    def generate_name(self):
        name: str = self.current_char
        while next(self) is not None:
            if self.current_char in WHITESPACE | set(':;\'",.') | {None}:
                break
            name += self.current_char
        return name
