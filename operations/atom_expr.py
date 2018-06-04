from typing import List, Tuple
from operations.operation import Operation
from operations.symbol_table import SymbolTable


class Factor(Operation):
    def __init__(self, atom: Atom, trailers: Tuple[Trailer]):
        self._atom = atom
        self._trailers = trailers

    def execute(self, symbolTables: List[SymbolTable]):
        pass