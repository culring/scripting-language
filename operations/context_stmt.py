from typing import List, Tuple

from operations.compound_stmt import CompoundStmt
from operations.operation import Operation
from operations.symbol_table import SymbolTable


class ContextStmt(Operation):
    @classmethod
    def createFromCompoundStmt(cls, compoundStmt: CompoundStmt) -> 'ContextStmt':
        obj = cls()
        obj._compoundStmt = compoundStmt

        return obj

    @classmethod
    def createFromSimpleStmt(cls, simpleStmt: SimpleStmt) -> 'ContextStmt':
        obj = cls()
        obj._simpleStmt = simpleStmt

        return obj

    def execute(self, symbolTables: List[SymbolTable]):
        pass
