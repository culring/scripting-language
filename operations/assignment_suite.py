from typing import List, Tuple

from operations.assignment_stmt import AssignmentStmt
from operations.operation import Operation
from operations.symbol_table import SymbolTable


class AssignmentSuite(Operation):
    def __init__(self, assignmentStmts: Tuple[AssignmentStmt] = None):
        self._assignmentStmts = assignmentStmts

    def execute(self, symbolTables: List[SymbolTable]):
        pass
