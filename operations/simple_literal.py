from typing import List

from operations.basic_list import BasicList
from operations.number import Number
from operations.operation import Operation
from operations.symbol_table import SymbolTable


class SimpleLiteral(Operation):
    @classmethod
    def createFromString(cls, string: str) -> 'SimpleLiteral':
        obj = cls()
        obj._value = string[1:-1]

        return obj

    @classmethod
    def createFromNumber(cls, number: Number) -> 'SimpleLiteral':
        obj = cls()
        obj._operation = number

        return obj

    @classmethod
    def createFromBool(cls, string: str) -> 'SimpleLiteral':
        obj = cls()
        obj._value = bool(string)

        return obj

    @classmethod
    def createFromNone(cls) -> 'SimpleLiteral':
        obj = cls()
        obj._value = None

        return obj

    @classmethod
    def createFromBasicList(cls, basicList: BasicList) -> 'SimpleLiteral':
        obj = cls()
        obj._operation = basicList

        return obj

    def execute(self, symbolTables: List[SymbolTable]):
        if hasattr(self, '_value'):
            return self._value
        elif hasattr(self, '_operation'):
            return self._operation.execute(symbolTables)
        else:
            raise AttributeError('SimpleLiteral cannot execute without proper attributes')
