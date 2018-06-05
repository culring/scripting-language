from typing import List, Tuple

from operations.arglist import Arglist
from operations.operation import Operation
from operations.suite import Suite
from operations.symbol_table import SymbolTable


class FuncdefStmt(Operation):
    def __init__(self, name: str, arglist: Arglist, suite: Suite):
        self._name = name
        self._arglist = arglist
        self._suite = suite

    def execute(self, symbolTables: List[SymbolTable]):
        pass
