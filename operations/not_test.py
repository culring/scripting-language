from typing import List
from operations.comparison import Comparison
from operations.operation import Operation
from operations.symbol_table import SymbolTable


class NotTest(Operation):
    @classmethod
    def createFromComparison(cls, comparison: Comparison):
        obj = cls()
        obj._comparison = comparison

        return obj

    @classmethod
    def createFromNotTest(cls, notTest: 'NotTest'):
        obj = cls()
        obj._notTest = notTest
        return obj

    def execute(self, symbolTables: List[SymbolTable]):
        if hasattr(self, '_comparison'):
            return self._comparison.execute(symbolTables)
        elif hasattr(self, '_notTest'):
            return self._notTest.execute(symbolTables)
        else:
            raise AttributeError('NotTest cannot execute without proper attributes')


