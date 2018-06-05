from typing import List
from operations.comparator import Comparator
from operations.operation import Operation
from operations.symbol_table import SymbolTable


class Comparison(Operation):
    @classmethod
    def createFromTwoExprs(cls, expr1: 'Expr', comparator: Comparator, expr2: 'Expr'):
        obj = cls()
        obj._expr1 = expr1
        obj._comparator = comparator
        obj._expr2 = expr2

        return obj

    @classmethod
    def createFromExpr(cls, expr: 'Expr'):
        obj = cls()
        obj._expr = expr

        return obj

    def execute(self, symbolTables: List[SymbolTable]):
        if hasattr(self, '_comparator'):
            return self._comparator.compare(self._expr1, self._expr2)
        elif hasattr(self, '_expr'):
            return bool(self._expr)
        else:
            raise AttributeError('Comparison cannot execute without proper attributes')