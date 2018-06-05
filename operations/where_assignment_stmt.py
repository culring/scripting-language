from typing import List, Tuple
from operations.operation import Operation
from operations.symbol_table import SymbolTable
from operations.where_assignment import WhereAssignment


class WhereAssignmentStmt(Operation):
    def __init__(self, whereAssignment: WhereAssignment):
        self._whereAssignment = whereAssignment

    def execute(self, symbolTables: List[SymbolTable]):
        pass
