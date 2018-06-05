from typing import List, Tuple

from operations.exceptions.unrecognised_token_error import UnrecognisedTokenError
from operations.operation import Operation
from operations.power import Power
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
        if hasattr(self, '_sign'):
            value = self._factor.execute(symbolTables)

            if self._sign == '+':
                return value
            elif self._sign == '-':
                return -value
            else:
                raise UnrecognisedTokenError("Factor cannot recognise 'sign' token")
        elif hasattr(self, '_power'):
            return self._power.execute(symbolTables)
        else:
            raise AttributeError("Factor do not have attributes necessary to execute")