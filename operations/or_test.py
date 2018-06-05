from typing import List
from operations.and_test import AndTest
from operations.operation import Operation
from operations.symbol_table import SymbolTable


class OrTest(Operation):
    def __init__(self, andTest1: AndTest, andTest2: AndTest = None):
        self._andTest1 = andTest1
        self._andTest2 = andTest2

    def execute(self, symbolTables: List[SymbolTable]):
        result = self._andTest1.execute(symbolTables)
        if self._andTest2:
            result = result and self._andTest2.execute(symbolTables)

        return result
