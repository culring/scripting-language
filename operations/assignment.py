from typing import List, Tuple

from operations.by_slice_list import BySliceList
from operations.expr import Expr
from operations.operation import Operation
from operations.symbol_table import SymbolTable


class Assignment(Operation):
    @classmethod
    def createFromExpr(cls, name: str, expr: Expr) -> 'Assignment':
        obj = cls()
        obj._name = name
        obj._expr = expr

        return obj

    @classmethod
    def createFromBySliceList(cls, name: str, bySliceList: BySliceList) -> 'Assignment':
        obj = cls()
        obj._name = name
        obj._bySliceList = bySliceList

        return obj

    def execute(self, symbolTables: List[SymbolTable]):
        if hasattr(self, '_expr'):
            value = self._expr.execute(symbolTables)
        # by slice list
        else:
            value = self._bySliceList.execute(symbolTables)

        try:
            table = SymbolTable.find(self._name, symbolTables)
        except Exception:
            table = symbolTables[-1]

        table[self._name] = value
