from typing import List, Tuple
from operations.operation import Operation
from operations.symbol_table import SymbolTable


class Term(Operation):
    def __init__(self, term: Factor, operations: Tuple[str, Factor] = None):
        self._term = term
        self._operations = operations

    def execute(self, symbolTables: List[SymbolTable]):
        pass
