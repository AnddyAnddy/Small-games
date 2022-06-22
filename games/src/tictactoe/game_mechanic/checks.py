from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Sequence

from src.tictactoe.game_mechanic.motif import Motif

if TYPE_CHECKING:
    from src.tictactoe.game_mechanic.board import Board


class Check(ABC):

    @abstractmethod
    def apply(self, board: Board) -> bool:
        ...

    @staticmethod
    def check_if_one_section_is_good(matrix: Sequence[Sequence[Motif]]):
        """Check if there is a sequence where all the motifs are identical, and they are not blank."""
        # todo: rename function
        return any(it[0] != Motif.BLANK and it.count(it[0]) == len(it) for it in matrix)


class CheckLine(Check):

    def apply(self, board: Board) -> bool:
        """Check if there is a line containing all the same motif but the blank one."""
        return Check.check_if_one_section_is_good(board.rows)


class CheckColumn(Check):

    def apply(self, board: Board) -> bool:
        """Check if there is a column containing all the same motif but the blank one."""
        return Check.check_if_one_section_is_good(board.columns)


class CheckDiagonals(Check):
    def apply(self, board: Board) -> bool:
        """Check if there is a diagonal containing all the same motif but the blank one."""
        return Check.check_if_one_section_is_good(board.diagonals)
