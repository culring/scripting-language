from typing import List
from operations.operation import Operation
from operations.symbol_table import SymbolTable


class ForStmt(Operation):
    def execute(self, symbolTables: List[SymbolTable]):
        raise NotImplementedError

    def __init__(self, name: str, expr: Expr, loopSuite: LoopSuite):
        self._name = name
        self._expr = expr
        self._loopSuite = loopSuite