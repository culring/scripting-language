from typing import List
from operations.operation import Operation
from operations.symbol_table import SymbolTable


class ForStmt(Operation):
    def __init__(self, name: str, expr: 'Expr', loopSuite: 'LoopSuite'):
        self._name = name
        self._expr = expr
        self._loopSuite = loopSuite

    def execute(self, symbolTables: List[SymbolTable]):
        initTable, contextStmts = self._loopSuite.execute(symbolTables)
        historyTable = HistoryTable(initTable)
        symbolTables.append(historyTable)
        for value in self._expr.execute(symbolTables):
            symbolTables.append(SymbolTable())
            symbolTables[-1][self._name] = value
            for stmt in contextStmts:
                stmt.execute(symbolTables)
            symbolTables.pop()
            symbolTables[-1].updateHistory()

class HistoryTable:
    class PreviousObject:
        def __init__(self, initValue):
            self._history = list()
            self._history.append(initValue)

        def __getitem__(self, item: int):
            if item < 1:
                item = 1
            elif item > len(self._history):
                item = len(self._history)

            return self._history[-item]

        def _addItem(self, item):
            self._history.append(item)

    def __getitem__(self, item):
        pass

    def __setitem__(self, key, value):
        pass

    def __contains__(self, item):
        return item in self._dict

    def __str__(self):
        return str(self._table)

    def __init__(self, table: SymbolTable):
        self._table = table
        for key, value in self._table.items():
            value = table[key]
            table[key] = self.PreviousObject(value)

    def updateHistory(self):
        for key, value in self.items():
            self._table[key].prev._addItem(value)
