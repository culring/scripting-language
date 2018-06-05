from typing import List, Tuple
from operations.operation import Operation
from operations.symbol_table import SymbolTable


class Number(Operation):
    @classmethod
    def createNonNegativeInteger(cls, string):
        obj = cls()
        obj._value = int(string)

        return obj

    @classmethod
    def createFloat(cls, string):
        obj = cls()
        obj._value = float(string)

        return obj

    def execute(self, symbolTables: List[SymbolTable]):
        return self._value
