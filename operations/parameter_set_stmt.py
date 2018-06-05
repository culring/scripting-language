from typing import List, Tuple
from operations.operation import Operation
from operations.parameter_set_suite import ParameterSetSuite
from operations.symbol_table import SymbolTable


class ParameterSetStmt(Operation):
    def __init__(self, name: str, parameterSetSuite: ParameterSetSuite):
        self._name = name
        self._parameterSetSuite = parameterSetSuite

    def execute(self, symbolTables: List[SymbolTable]):
        pass
