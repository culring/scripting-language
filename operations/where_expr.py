from typing import List, Tuple
from operations.operation import Operation
from operations.symbol_table import SymbolTable


class WhereExpr(Operation):
    @classmethod
    def createFromName(cls, bySliceList: BySliceList, name: str) -> 'WhereExpr':
        obj = cls()
        obj._bySliceList = bySliceList
        obj._name = name

        return obj

    @classmethod
    def createFromSimpleLambda(cls, bySliceList: BySliceList, simpleLambda: SimpleLambda) -> 'WhereExpr':
        obj = cls()
        obj._bySliceList = bySliceList
        obj._simpleLambda = simpleLambda

        return obj

    def execute(self, symbolTables: List[SymbolTable]):
        pass
