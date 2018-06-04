from typing import List, Tuple
from operations.operation import Operation
from operations.power import Power
from operations.symbol_table import SymbolTable


class Atom(Operation):
    @classmethod
    def createFromName(cls, name: str) -> 'Atom':
        obj = cls()
        obj._name = name

        return obj

    @classmethod
    def createFromSimpleLiteral(cls, simpleLiteral: SimpleLiteral) -> 'Atom':
        obj = cls()
        obj._simpleLiteral = simpleLiteral

        return obj

    def execute(self, symbolTables: List[SymbolTable]):
        pass