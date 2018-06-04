from typing import List, Tuple
from operations.operation import Operation
from operations.symbol_table import SymbolTable


class ParameterSetSuite(Operation):
    def __init__(self, stmts = None):
        self._stmts = stmts

    def execute(self, symbolTables: List[SymbolTable]):
        pass
