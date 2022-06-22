from typing import TYPE_CHECKING, Sequence

from src.tictactoe.game_mechanic.checks import CheckLine, CheckColumn, CheckDiagonals
from src.tictactoe.game_mechanic.motif import Motif

if TYPE_CHECKING:
    from src.tictactoe.game_mechanic.checks import Check


class Board:
    def __init__(self):
        self.size = 3
        self.board: list[list[Motif]] = [[Motif.BLANK] * self.size for _ in range(self.size)]
        self._checks: list[Check] = [CheckLine(), CheckDiagonals(), CheckColumn()]
        self.motif_count = 0

    @property
    def rows(self) -> Sequence[Sequence[Motif]]:
        return self.board

    @property
    def columns(self) -> Sequence[Sequence[Motif]]:
        return list(zip(*self.board))

    @property
    def diagonals(self) -> Sequence[Sequence[Motif]]:
        return [[self.board[i][i] for i in range(self.size)], [row[-i - 1] for i, row in enumerate(self.board)]]

    @property
    def is_fully_filled(self) -> bool:
        return self.size ** 2 == self.motif_count

    def checks(self) -> bool:
        """Return True when any check is valid."""
        return any(check.apply(self) for check in self._checks)

    def update(self, motif: Motif, x: int, y: int):
        """Update the board with a new play in (x, y) position with the motif."""
        # todo: raise ValueError instead of assert
        assert 0 <= x < self.size
        assert 0 <= y < self.size
        assert motif in Motif and motif != Motif.BLANK
        assert self.board[x][y] == Motif.BLANK
        self.board[x][y] = motif
        self.motif_count += 1

    def __str__(self):
        # TODO: improve complexity
        s = ""
        for line in self.board:
            for motif in line:
                s += f"{motif} "
            s += "\n"
        return s
