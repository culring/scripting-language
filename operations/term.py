from typing import List, Tuple

from operations.atom_expr import Factor
from operations.operation import Operation
from operations.symbol_table import SymbolTable

from .exceptions.unrecognised_token_error import UnrecognisedTokenError


class Term(Operation):
    def __init__(self, term: Factor, operations: Tuple[Tuple[str, Factor], ...] = ()):
        self._term = term
        self._operations = operations

    def execute(self, symbolTables: List[SymbolTable]):
        # (STAR | SLASH | PERCENT | '//')
        value = self._term.execute(symbolTables)
        for operator, operand in self._operations:
            currValue = operand.execute(symbolTables)
            if operator == '*':
                value *= currValue
            elif operator == '/':
                value /= currValue
            elif operator == '%':
                value %= currValue
            elif operator == '//':
                value //= currValue
            else:
                raise UnrecognisedTokenError()
