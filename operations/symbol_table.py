from typing import List

from .exceptions.symbol_not_found_error import SymbolNotFoundError


class SymbolTable:
    def __init__(self):
        self._dict = dict()

    def __getitem__(self, key):
        return self._dict[key]

    def __setitem__(self, key, value):
        self._dict[key] = value

    def __contains__(self, item):
        return item in self._dict

    def __str__(self):
        return str(self._dict)

    @staticmethod
    def find(symbol, tables: List['SymbolTable']):
        for table in tables[::-1]:
            if symbol in table:
                return table

        raise SymbolNotFoundError()
