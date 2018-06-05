from typing import List, Tuple

from operations.assignment import Assignment
from operations.operation import Operation
from operations.symbol_table import SymbolTable


class AssignmentStmt(Operation):
    def __init__(self, assignment: Assignment):
        self._assignment = assignment

    def execute(self, symbolTables: List[SymbolTable]):
        self._assignment.execute(symbolTables)
