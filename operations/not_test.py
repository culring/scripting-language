from typing import List
from operations.comparison import Comparison
from operations.operation import Operation
from operations.symbol_table import SymbolTable


class NotTest(Operation):
    @classmethod
    def createFromComparison(cls, comparison: Comparison):
        pass

    @classmethod
    def createFromNotTest(cls, notTest: 'NotTest'):
        currNotTest = cls()
        currNotTest._notTest = notTest
        return currNotTest

    def execute(self, symbolTables: List[SymbolTable]):
        pass


