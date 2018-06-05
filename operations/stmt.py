from typing import List, Tuple

from operations.context_stmt import ContextStmt
from operations.funcdef_stmt import FuncdefStmt
from operations.operation import Operation
from operations.parameter_set_stmt import ParameterSetStmt
from operations.symbol_table import SymbolTable


class Stmt(Operation):
    @classmethod
    def createFromContextStmt(cls, contextStmt: ContextStmt) -> 'Stmt':
        obj = cls()
        obj._contextStmt = contextStmt

        return obj

    @classmethod
    def createFromFuncdefStmt(cls, funcdefStmt: FuncdefStmt) -> 'Stmt':
        obj = cls()
        obj._funcdefStmt = funcdefStmt
        return obj

    @classmethod
    def createFromParameterSetStmt(cls, parameterSetStmt: ParameterSetStmt) -> 'Stmt':
        obj = cls()
        obj._parameterSetStmt = parameterSetStmt
        
        return obj

    def execute(self, symbolTables: List[SymbolTable]):
        print("hello stmt!")

        if hasattr(self, '_contextStmt'):
            self._contextStmt.execute(symbolTables)
        elif hasattr(self, '_funcdefStmt'):
            raise NotImplementedError()
        elif hasattr(self, '_parameterSetStmt'):
            raise NotImplementedError()
        else:
            raise AttributeError('Stmt cannot execute without proper attributes')
