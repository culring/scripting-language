from typing import List
from operations.comparison import NotTest
from operations.operation import Operation
from operations.symbol_table import SymbolTable


class AndTest(Operation):
    def __init__(self, notTest1: NotTest, notTest2: NotTest = None):
        self._notTest1 = notTest1
        self._notTest2 = notTest2

    def execute(self, symbolTables: List[SymbolTable]):
        pass