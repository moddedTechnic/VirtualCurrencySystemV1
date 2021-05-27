from typing import Iterable

from .tokens import Token, TokenType


class Parser:
    def __init__(self, tokens: Iterable[Token]):
        self.tokens = iter(tokens)
        self.current_token: Optional[str] = None

    def __iter__(self):
        yield next(self)
        while next(self) is not None:
            yield self.current_token

    def __next__(self):
        try:
            self.current_token = next(self.tokens)
            if self.current_token.type == TokenType.WHITESPACE:
                next(self)
        except StopIteration:
            self.current_token = None
        return self.current_token

    def __call__(self):
        for token in self:
            yield self.visit(token)

    def visit(self, token):
        return self.visit_ruleset()

    def visit_ruleset(self):
        names = [self.current_token]
        while next(self) is not None and self.current_token.type == TokenType.NAME:
            names.append(self.current_token)
        print(self.current_token)
        # print(names)
