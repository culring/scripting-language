from typing import List, Tuple

from operations.operation import Operation
from operations.symbol_table import SymbolTable


class BasicList(Operation):
    def __init__(self, exprs: Tuple['Expr'] = None):
        self._exprs = exprs

    def execute(self, symbolTables: List[SymbolTable]):
        pass
