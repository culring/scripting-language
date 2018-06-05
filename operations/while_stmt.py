from typing import List

from operations.loop_suite import LoopSuite
from operations.operation import Operation
from operations.or_test import OrTest
from operations.symbol_table import SymbolTable


class WhileStmt(Operation):
    def __init__(self, orTest: OrTest, loopSuite: LoopSuite):
        self._orTest = orTest
        self._loopSuite = loopSuite

    def execute(self, symbolTables: List[SymbolTable]):
        pass
