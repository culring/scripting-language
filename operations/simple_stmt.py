from typing import List, Tuple

from operations.assignment_stmt import AssignmentStmt
from operations.import_stmt import ImportStmt
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
        if hasattr(self, '_importStmt'):
            raise NotImplementedError()
        elif hasattr(self, '_expr'):
            self._expr.execute(symbolTables)
        elif hasattr(self, '_assignmentStmt'):
            raise NotImplementedError()
        else:
            raise AttributeError('SimpleStmt cannot execute without proper attributes')