from typing import List, Tuple

from operations.operation import Operation
from operations.simple_literal import SimpleLiteral
from operations.symbol_table import SymbolTable


class Argument(Operation):
    @classmethod
    def createFromSimpleLiteral(cls, simpleLiteral: SimpleLiteral) -> 'Argument':
        obj = cls()
        obj._simpleLiteral = simpleLiteral

        return obj

    @classmethod
    def createFromName(cls, name: str) -> 'Argument':
        obj = cls()
        obj._name = name

        return obj

    def execute(self, symbolTables: List[SymbolTable]):
        if hasattr(self, '_simpleLiteral'):
            return self._simpleLiteral.execute()
        elif hasattr(self, '_name'):
            return SymbolTable.find(self._name, symbolTables)[self._name]
        else:
            raise AttributeError('Argument cannot execute without proper attributes')