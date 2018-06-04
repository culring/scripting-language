from typing import List, Tuple

from operations.expr import Expr
from operations.operation import Operation
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

    @classmethod
    def createFromExpr(cls, name: str, expr: Expr) -> 'Argument':
        obj = cls()
        obj._name = name
        obj._expr = expr

        return obj

    def execute(self, symbolTables: List[SymbolTable]):
        pass