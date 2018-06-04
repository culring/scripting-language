from typing import List, Tuple
from operations.operation import Operation
from operations.symbol_table import SymbolTable


class Number(Operation):
    def __init__(self, value):
        self._value = value

    def execute(self, symbolTables: List[SymbolTable]):
        pass
