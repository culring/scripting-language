from typing import List, Tuple
from operations.operation import Operation
from operations.term import Term
from operations.symbol_table import SymbolTable


class Expr(Operation):
    def __init__(self, term: Term, rest: Tuple[Tuple[Operator, Term]] = None):
        self._term = term
        self._rest = rest

    def execute(self, symbolTables: List[SymbolTable]):
        pass