from enum import Enum, auto


class Comparator:
    class Type(Enum):
        LESS = auto()
        GREATER = auto()
        DOUBLEEQUAL = auto()
        LESSEQUAL = auto()
        GREATEREQUAL = auto()
        NOTEQUAL = auto()

    @property
    def type(self):
        return self._type

    def __init__(self, type: Type):
        self._type = type