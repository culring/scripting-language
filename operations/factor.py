from typing import List, Tuple
from operations.operation import Operation
from operations.symbol_table import SymbolTable


class Factor(Operation):
    @classmethod
    def createFromFactor(cls, sign: str, factor: 'Factor') -> 'Factor':
        obj = cls()
        obj._sign = sign
        obj._factor = factor

        return obj

    @classmethod
    def createFromPower(cls, power: Power) -> 'Factor':
        obj = cls()
        obj._power = power

        return obj

    def execute(self, symbolTables: List[SymbolTable]):
        pass