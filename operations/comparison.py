from typing import List
from operations.comparator import Comparator
from operations.operation import Operation
from operations.symbol_table import SymbolTable


class Comparison(Operation):
    @classmethod
    def createFromTwoExprs(cls, expr1: Expr, comparator: Comparator, expr2: Expr):
        currNotTest = cls()
        currNotTest._expr1 = expr1
        currNotTest._comparator = comparator
        currNotTest._expr2 = expr2

    @classmethod
    def createFromExpr(cls, expr: Expr):
        currNotTest = cls()
        currNotTest._expr = expr

    def execute(self, symbolTables: List[SymbolTable]):
        pass