from typing import List, Tuple
from operations.operation import Operation
from operations.symbol_table import SymbolTable
from operations.where_expr import WhereExpr


class WhereAssignment(Operation):
    def __init__(self, name: str, whereExpr: WhereExpr):
        self._name = name
        self._whereExpr = whereExpr

    def execute(self, symbolTables: List[SymbolTable]):
        pass
