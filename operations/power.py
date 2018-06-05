from typing import List, Tuple

from operations.atom_expr import AtomExpr
from operations.factor import Factor
from operations.operation import Operation
from operations.symbol_table import SymbolTable


class Power(Operation):
    def __init__(self, atomExpr: AtomExpr, factor: Factor = None):
        self._atomExpr = atomExpr
        self._factor = factor

    def execute(self, symbolTables: List[SymbolTable]):
        value = self._atomExpr.execute(symbolTables)
        if self._factor:
            value **= self._factor.execute(symbolTables)

        return value
