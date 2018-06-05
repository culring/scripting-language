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
        orTestResult = self._orTest.execute(symbolTables)
        if orTestResult:
            symbolTables.append(SymbolTable())
            self._suite.execute(symbolTables)
            symbolTables.pop()
        else:
            if self._elseStmt:
                symbolTables.append(SymbolTable())
                self._elseStmt.execute(symbolTables)
                symbolTables.pop()
