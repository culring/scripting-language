from typing import List, Tuple
from operations.operation import Operation
from operations.symbol_table import SymbolTable


class Trailer(Operation):
    @classmethod
    def createFromArglist(cls, arglist: Arglist = None) -> 'Trailer':
        obj = cls()
        obj._arglist = arglist

        return obj

    @classmethod
    def createFromAccess(cls, integer: int) -> 'Trailer':
        obj = cls()
        obj._integer = integer

        return obj

    @classmethod
    def createFromDotName(cls, name: str) -> 'Trailer':
        obj = cls()
        obj._name = name

        return obj

    def execute(self, symbolTables: List[SymbolTable]):
        pass