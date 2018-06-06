from typing import List
from operations.operation import Operation
from operations.symbol_table import SymbolTable


class ForStmt(Operation):
    def __init__(self, name: str, expr: 'Expr', loopSuite: 'LoopSuite'):
        self._name = name
        self._expr = expr
        self._loopSuite = loopSuite

    # def execute(self, symbolTables: List[SymbolTable]):
    #     initTable, contextStmts = self._loopSuite.execute(symbolTables)
    #     symbolTables.append(initTable)
    #     for value in self._expr.execute(symbolTables):
    #         symbolTables[-1][self._name] = value
    #         for stmt in contextStmts:
    #             stmt.execute(symbolTables)
    #     symbolTables.pop()

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
        symbolTables.pop()


class HistoryTable(SymbolTable):
    class PreviousObject:
        class History:
            def __init__(self, initValue):
                self._history = list()
                self._history.append(initValue)

            def __getitem__(self, item: int):
                if item < 1:
                    item = 1
                elif item > len(self._history):
                    item = len(self._history)

                return self._history[-item]

            def update(self, value):
                self._history.append(value)

        def __init__(self, initValue):
            self._history = self.History(initValue)
            self._value = initValue

        def __getattr__(self, item):
            if item == 'prev':
                return self._history

        def update(self):
            self._history.update(self._value)

        @property
        def value(self):
            return self._value

        @value.setter
        def value(self, value):
            self._value = value

    def __init__(self, table: SymbolTable):
        super().__init__()
        self._dict = table
        for key, value in self._dict.items():
            table[key] = self.PreviousObject(value)

    def __setitem__(self, key, value):
        self._dict[key].value = value

    def updateHistory(self):
        for key, value in self.items():
            self._dict[key].update()
