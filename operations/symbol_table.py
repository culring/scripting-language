from enum import Enum, auto


class SymbolTable:
    class Type(Enum):
        # values
        INT = auto()
        LIST = auto()
        STRING = auto()
        FLOAT = auto()
        BOOL = auto()
        OBJECT = auto()
        # values

        # declarations
        FUNCTION = auto()
        PARAMETER_SET = auto()
        # declarations

    def __init__(self):
        self._dict = dict()

    def __getitem__(self, key):
        return self._dict[key]

    def __setitem__(self, key, value):
        self._dict[key] = value
