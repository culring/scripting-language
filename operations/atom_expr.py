from typing import List, Tuple

from operations.atom import Atom
from operations.operation import Operation
from operations.symbol_table import SymbolTable
from operations.trailer import Trailer


class AtomExpr(Operation):
    def __init__(self, atom: Atom, trailers: Tuple[Trailer, ...] = ()):
        self._atom = atom
        self._trailers = trailers

    def execute(self, symbolTables: List[SymbolTable]):
        value = self._atom.execute(symbolTables)

        for trailer in self._trailers:
            value = trailer.exe
