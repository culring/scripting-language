from typing import List
from operations.not_test import NotTest
from operations.operation import Operation
from operations.symbol_table import SymbolTable


class AndTest(Operation):
    def __init__(self, notTest1: NotTest, notTest2: NotTest = None):
        self._notTest1 = notTest1
        self._notTest2 = notTest2

    def execute(self, symbolTables: List[SymbolTable]):
        result = self._notTest1.execute(symbolTables)
        if self._notTest2:
            result = result and self._notTest2.execute(symbolTables)

        return result