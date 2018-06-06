from typing import List, Tuple

import itertools

from operations.atom import Atom
from operations.exceptions.prev_object_error import PrevObjectError
from operations.for_stmt import HistoryTable
from operations.operation import Operation
from operations.symbol_table import SymbolTable
from operations.trailer import Trailer


class AtomExpr(Operation):
    def __init__(self, atom: Atom, trailers: Tuple[Trailer, ...] = ()):
        self._atom = atom
        self._trailers = trailers

    def execute(self, symbolTables: List[SymbolTable]):
        value = self._atom.execute(symbolTables)

        iterator = iter(self._trailers)
        for index, trailer in enumerate(iterator):
            if type(value) == HistoryTable.PreviousObject:
                if trailer.isDotNameType():
                    trailerType = trailer.getDotNameType()
                    if trailerType == 'prev':
                        try:
                            nextTrailer = self._trailers[index+1]
                            if nextTrailer.isAccessType():
                                value = trailer.execute(symbolTables, value)
                            else:
                                raise PrevObjectError("Prev object cannot be called nor "
                                                      "cannot be accessed for attributes.")
                        except IndexError:
                            raise PrevObjectError("Prev object cannot be accessed directly.")
                else:
                    value = trailer.execute(symbolTables, value.value)
            else:
                value = trailer.execute(symbolTables, value)

        if type(value) == HistoryTable.PreviousObject:
            value = value.value

        return value
