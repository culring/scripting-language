from typing import List, Tuple
from operations.operation import Operation
from operations.symbol_table import SymbolTable


class Arglist(Operation):
    def __init__(self, argument: Argument, rest: Tuple[Argument] = None):
        self._argument = argument
        self._rest = rest

    def execute(self, symbolTables: List[SymbolTable]):
        pass
