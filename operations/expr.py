from typing import List, Tuple

from operations.operation import Operation
from operations.term import Term
from operations.symbol_table import SymbolTable
from .exceptions.unrecognised_token_error import UnrecognisedTokenError


class Expr(Operation):
    def __init__(self, term: Term, rest: Tuple[Tuple[str, Term]] = ()):
        self._term = term
        self._rest = rest

    def execute(self, symbolTables: List[SymbolTable]):
        value = self._term.execute(symbolTables)
        for operator, operand in self._rest:
            operandValue = operand.execute(symbolTables)
            if operator == '+':
                value += operandValue
            elif operator == '-':
                value -= operandValue
            else:
                raise UnrecognisedTokenError()

        return value
