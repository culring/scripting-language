from typing import List, Tuple

from operations.assignment_suite import AssignmentSuite
from operations.operation import Operation
from operations.parameter_set_suite import ParameterSetSuite
from operations.suite import Suite
from operations.symbol_table import SymbolTable


class LoopSuite(Operation):
    def __init__(self, suite: Suite, assignmentSuite: AssignmentSuite = None):
        self._suite = suite
        self._assignmentSuite = assignmentSuite

    def execute(self, symbolTables: List[SymbolTable]):
        pass
