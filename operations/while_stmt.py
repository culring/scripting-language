from typing import List
from operations.operation import Operation
from operations.symbol_table import SymbolTable


class WhileStmt(Operation):
    def __init__(self, orTest: OrTest, loopSuite: LoopSuite):
        self._orTest = orTest
        self._loopSuite = loopSuite

    def execute(self, symbolTables: List[SymbolTable]):
        pass
