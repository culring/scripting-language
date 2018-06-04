from typing import List, Tuple
from operations.operation import Operation
from operations.symbol_table import SymbolTable


class CompoundStmt(Operation):
    @classmethod
    def createFromForStmt(cls, forStmt: ForStmt) -> 'CompoundStmt':
        obj = cls()
        obj._forStmt = forStmt

        return obj

    @classmethod
    def createFromWhileStmt(cls, whileStmt: WhileStmt) -> 'CompoundStmt':
        obj = cls()
        obj._whileStmt = whileStmt

        return obj

    @classmethod
    def createFromIfStmt(cls, ifStmt: IfStmt) -> 'CompoundStmt':
        obj = cls()
        obj._ifStmt = ifStmt

        return obj

    def execute(self, symbolTables: List[SymbolTable]):
        pass