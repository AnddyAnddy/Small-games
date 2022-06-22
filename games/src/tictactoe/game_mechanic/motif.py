from enum import Enum


class Motif(Enum):
    CROSS = "X"
    CIRCLE = "O"
    BLANK = "_"

    def __str__(self):
        return self.value
