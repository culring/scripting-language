from typing import List
from operations.operation import Operation
from operations.symbol_table import SymbolTable


class Suite(Operation):
    def __init__(self, contextStmts: Tuple[ContextStmt] = None):
        self._contextStmt = contextStmts

    def execute(self, symbolTables: List[SymbolTable]):
        pass