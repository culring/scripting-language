from typing import List, Tuple
from operations.operation import Operation
from operations.symbol_table import SymbolTable


class CompoundStmt(Operation):
    @classmethod
    def createFromForStmt(cls, forStmt: 'ForStmt') -> 'CompoundStmt':
        obj = cls()
        obj._forStmt = forStmt

        return obj

    @classmethod
    def createFromWhileStmt(cls, whileStmt: 'WhileStmt') -> 'CompoundStmt':
        obj = cls()
        obj._whileStmt = whileStmt

        return obj

    @classmethod
    def createFromIfStmt(cls, ifStmt: 'IfStmt') -> 'CompoundStmt':
        obj = cls()
        obj._ifStmt = ifStmt

        return obj

    def execute(self, symbolTables: List[SymbolTable]):
        if hasattr(self, '_forStmt'):
            self._forStmt.execute(symbolTables)
        elif hasattr(self, '_whileStmt'):
            pass
        elif hasattr(self, '_ifStmt'):
            self._ifStmt.execute(symbolTables)
        else:
            raise AttributeError('CompoundStmt cannot execute without proper attributes')