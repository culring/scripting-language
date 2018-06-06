from typing import List, Tuple

import sys

from operations.operation import Operation
from operations.stmt import Stmt
from operations.symbol_table import SymbolTable


class Script(Operation):
    def __init__(self, stmts: Tuple[Stmt, ...] = ()):
        self._stmts = stmts

    def execute(self, symbolTables: List[SymbolTable]):
        for lineNumber, stmt in enumerate(self._stmts, 1):
            stmt.execute(symbolTables)
            # try:
            #     stmt.execute(symbolTables)
            # except Exception as e:
            #     print(f'Semantic error: {e.args[0] if e.args else "Unknown error occurred"}', file=sys.stderr)
