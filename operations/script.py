from typing import List, Tuple

from operations.operation import Operation
from operations.stmt import Stmt
from operations.symbol_table import SymbolTable


class Script(Operation):
    def __init__(self, stmts: Tuple[Stmt, ...] = ()):
        self._stmts = stmts

    def execute(self, symbolTables: List[SymbolTable]):
        for stmt in self._stmts:
            stmt.execute(symbolTables)
