from typing import List, Tuple

from operations.context_stmt import ContextStmt
from operations.operation import Operation
from operations.symbol_table import SymbolTable


class Suite(Operation):
    def __init__(self, contextStmts: Tuple[ContextStmt, ...] = None):
        self._contextStmt = contextStmts

    def execute(self, symbolTables: List[SymbolTable]):
        symbolTables.append(SymbolTable())
        for stmt in self._contextStmt:
            stmt.execute(symbolTables)
        symbolTables.pop()
