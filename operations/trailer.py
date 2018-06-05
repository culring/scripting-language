from typing import List, Tuple

from operations.symbol_table import SymbolTable


class Trailer:
    @classmethod
    def createFromArglist(cls, arglist: 'Arglist' = None) -> 'Trailer':
        obj = cls()
        obj._arglist = arglist

        return obj

    @classmethod
    def createFromAccess(cls, integer: str) -> 'Trailer':
        obj = cls()
        obj._integer = int(integer)

        return obj

    @classmethod
    def createFromDotName(cls, name: str) -> 'Trailer':
        obj = cls()
        obj._name = name

        return obj

    def execute(self, symbolTables: List[SymbolTable], obj):
        if hasattr(self, '_arglist'):
            if self._arglist:
                arglist = self._arglist.execute(symbolTables)
                return obj(*arglist)
            else:
                return obj()
        elif hasattr(self, '_integer'):
            return obj[self._integer]
        elif hasattr(self, '_name'):
            return getattr(obj, self._name)
        else:
            raise AttributeError('Trailer cannot execute because of wrong attributes')