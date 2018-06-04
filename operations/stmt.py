from typing import List, Tuple
from operations.operation import Operation
from operations.symbol_table import SymbolTable


class Stmt(Operation):
    @classmethod
    def createFromContextStmt(cls, contextStmt: ContextStmt) -> 'Stmt':
        obj = cls()
        obj._contextStmt = contextStmt

        return obj

    def createFromFuncdefStmt(cls, funcdefStmt: FuncdefStmt) -> 'Stmt':
        obj = cls()
        obj._funcdefStmt = funcdefStmt
        return obj

    def createFromParameterSetStmt(cls, parameterSetStmt: ParameterSetStmt) -> 'Stmt':
        obj = cls()
        obj._parameterSetStmt = parameterSetStmt
        
        return obj

    def execute(self, symbolTables: List[SymbolTable]):
        pass