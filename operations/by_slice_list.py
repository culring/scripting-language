from typing import List, Tuple

from operations.expr import Expr
from operations.operation import Operation
from operations.symbol_table import SymbolTable


class BySliceList(Operation):
    def __init__(self, expr1: Expr, expr2: Expr, expr3: Expr = None):
        self._expr1 = expr1
        self._expr2 = expr2
        self._expr3 = expr3

    def execute(self, symbolTables: List[SymbolTable]):
        pass