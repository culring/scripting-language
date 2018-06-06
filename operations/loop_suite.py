from typing import List, Tuple

from operations.assignment_suite import AssignmentSuite
from operations.context_stmt import ContextStmt
from operations.operation import Operation
from operations.parameter_set_suite import ParameterSetSuite
from operations.suite import Suite
from operations.symbol_table import SymbolTable


class LoopSuite(Operation):
    def __init__(self, assignmentSuite: AssignmentSuite = None, contextStmts: Tuple[ContextStmt, ...] = ()):
        self._assignmentSuite = assignmentSuite
        self._contextStmts = contextStmts

    def execute(self, symbolTables: List[SymbolTable]):
        symbolTable = self._assignmentSuite.execute(symbolTables) if self._assignmentSuite else SymbolTable()
        return symbolTable, self._contextStmts
