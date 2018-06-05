from typing import List

from operations.else_stmt import ElseStmt
from operations.operation import Operation
from operations.or_test import OrTest
from operations.suite import Suite
from operations.symbol_table import SymbolTable


class IfStmt(Operation):
    def __init__(self, orTest: OrTest, suite: Suite, elseStmt: ElseStmt = None):
        self._orTest = orTest
        self._suite = suite
        self._elseStmt = elseStmt

    def execute(self, symbolTables: List[SymbolTable]):
        pass