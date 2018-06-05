from typing import List, Tuple
from operations.operation import Operation
from operations.symbol_table import SymbolTable


class ImportStmt(Operation):
    def __init__(self, dottedName: 'DottedName'):
        self._dottedName = dottedName

    def execute(self, symbolTables: List[SymbolTable]):
        pass
