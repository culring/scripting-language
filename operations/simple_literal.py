from typing import List, Tuple

from operations.basic_list import BasicList
from operations.number import Number
from operations.operation import Operation
from operations.symbol_table import SymbolTable


class SimpleLiteral(Operation):
    @classmethod
    def createFromString(cls, string: str) -> 'SimpleLiteral':
        obj = cls()
        obj._value = string

        return obj

    @classmethod
    def createFromNumber(cls, number: Number) -> 'SimpleLiteral':
        obj = cls()
        obj._number = number

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
        obj._basicList = basicList

        return obj

    def execute(self, symbolTables: List[SymbolTable]):
        pass
