from typing import List
from operations.symbol_table import SymbolTable


class Operation:
    def execute(self, symbolTables: List[SymbolTable]):
        raise NotImplementedError
