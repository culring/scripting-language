from typing import List, Tuple
from operations.operation import Operation
from operations.symbol_table import SymbolTable


class SimpleLambda(Operation):
    def __init__(self, name: str, expr: Expr):
        self._name = name
        self._expr = expr

    def execute(self, symbolTables: List[SymbolTable]):
        pass
