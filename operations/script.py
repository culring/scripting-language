from typing import List, Tuple

from operations.operation import Operation
from operations.stmt import Stmt
from operations.symbol_table import SymbolTable


class Term(Operation):
    def __init__(self, stmts: Stmt):
        self._stmts = stmts

    def execute(self, symbolTables: List[SymbolTable]):
        pass
