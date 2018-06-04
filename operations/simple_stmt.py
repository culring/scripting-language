from typing import List, Tuple
from operations.operation import Operation
from operations.symbol_table import SymbolTable


class SimpleStmt(Operation):
    @classmethod
    def createFromImportStmt(cls, importStmt: ImportStmt) -> 'SimpleStmt':
        obj = cls()
        obj._importStmt = importStmt

        return obj

    @classmethod
    def createFromExpr(cls, expr: Expr) -> 'SimpleStmt':
        obj = cls()
        obj._expr = expr

        return obj

    @classmethod
    def createFromAssignmentStmt(cls, assignmentStmt: AssignmentStmt) -> 'SimpleStmt':
        obj = cls()
        obj._assignmentStmt =assignmentStmt

        return obj

    def execute(self, symbolTables: List[SymbolTable]):
        pass