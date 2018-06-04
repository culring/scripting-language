from typing import List, Tuple
from operations.operation import Operation
from operations.symbol_table import SymbolTable


class WhereAssignmentStmt(Operation):
    def __init__(self, whereAssignment: WhereAssigment):
        self._whereAssignment = whereAssignment

    def execute(self, symbolTables: List[SymbolTable]):
        pass
