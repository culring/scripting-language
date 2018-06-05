from typing import List, Tuple

from operations.argument import Argument
from operations.operation import Operation
from operations.symbol_table import SymbolTable


class Arglist(Operation):
    def __init__(self, arguments: Tuple[Argument, ...] = ()):
        print(f'arglist = {arguments}')
        self._arguments = arguments

    def execute(self, symbolTables: List[SymbolTable]):
        return [argument.execute(symbolTables) for argument in self._arguments]
