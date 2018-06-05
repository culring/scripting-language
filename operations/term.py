from typing import List, Tuple

from operations.factor import Factor
from operations.operation import Operation
from operations.symbol_table import SymbolTable

from .exceptions.unrecognised_token_error import UnrecognisedTokenError


class Term(Operation):
    def __init__(self, factor: Factor, operations: Tuple[Tuple[str, Factor], ...] = ()):
        self._factor = factor
        self._operations = operations

    def execute(self, symbolTables: List[SymbolTable]):
        value = self._factor.execute(symbolTables)

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

        return value
