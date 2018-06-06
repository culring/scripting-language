from typing import List
from operations.operation import Operation
from operations.simple_literal import SimpleLiteral
from operations.symbol_table import SymbolTable, SymbolNotFoundError


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
        if hasattr(self, '_simpleLiteral'):
            return self._simpleLiteral.execute(symbolTables)
        if hasattr(self, '_name'):
            try:
                table = SymbolTable.find(self._name, symbolTables)
                return table[self._name]
            except SymbolNotFoundError:
                if self._name == 'print':
                    return print
                if self._name == 'range':
                    return range
                else:
                    raise SymbolNotFoundError(f"Reference \'{self._name}\' not recognised.")
