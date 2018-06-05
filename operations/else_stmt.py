from typing import List, Tuple

from operations.operation import Operation
from operations.suite import Suite
from operations.symbol_table import SymbolTable


class ElseStmt(Operation):
    @classmethod
    def createFromSuite(cls, suite: Suite):
        obj = cls()
        obj._suite = suite

        return obj

    @classmethod
    def createFromIfStmt(cls, ifStmt: 'IfStmt'):
        obj = cls()
        obj._ifStmt = ifStmt

        return obj

    def execute(self, symbolTables: List[SymbolTable]):
        pass
