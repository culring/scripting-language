from typing import List, Tuple
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
        pass
