from enum import Enum, auto


class Comparator:
    class Type(Enum):
        LESS = auto()
        GREATER = auto()
        DOUBLEEQUAL = auto()
        LESSEQUAL = auto()
        GREATEREQUAL = auto()
        NOTEQUAL = auto()

    def compare(self, x, y):
        if self._type == self.Type.LESS:
            return x < y
        elif self._type == self.Type.GREATER:
            return x > y
        elif self._type == self.Type.DOUBLEEQUAL:
            return x == y
        elif self._type == self.Type.LESSEQUAL:
            return x <= y
        elif self._type == self.Type.GREATEREQUAL:
            return x >= y
        elif self._type == self.Type.NOTEQUAL:
            return x != y
        else:
            raise NotImplementedError("Comparator cannot compare with such comparator sign")

    @property
    def type(self):
        return self._type

    def __init__(self, type: Type):
        self._type = type