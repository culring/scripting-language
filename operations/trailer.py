from typing import List, Tuple

from operations.arglist import Arglist
from operations.symbol_table import SymbolTable

class Trailer():
    @classmethod
    def createFromArglist(cls, arglist: Arglist = None) -> 'Trailer':
        obj = cls()
        obj._arglist = arglist

        return obj

    @classmethod
    def createFromAccess(cls, integer: int) -> 'Trailer':
        obj = cls()
        obj._integer = integer

        return obj

    @classmethod
    def createFromDotName(cls, name: str) -> 'Trailer':
        obj = cls()
        obj._name = name

        return obj

    def execute(self, symbolTables: List[SymbolTable], object):
        if hasattr(self, '_arglist'):
            if self._arglist:
                arglist = self._arglist.execute(symbolTables)
                return object(*arglist)
            else:
                return object()
        elif hasattr(self, '_integer'):
            return object[self._integer]
        elif hasattr(self, '_name'):
            return getattr(object, self._name)
        else:
            raise AttributeError('Trailer cannot execute because of wrong attributes')