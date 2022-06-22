import itertools

from src.tictactoe.game_mechanic.board import Board
from src.tictactoe.game_mechanic.motif import Motif
from src.tictactoe.user_interface.ui_abstract import UI


class AllMoves(UI):

    ALL_MOVES = list(itertools.permutations([(i, j) for i in range(3) for j in range(3)]))

    def __init__(self, board: Board, test_index=0):
        super().__init__(board)
        self.turn = 0
        self.test_index = test_index

    def display(self):
        pass

    def display_winner(self, winner: Motif):
        pass

    def display_draw(self):
        pass

    def play(self, player: Motif):
        """Select the next move to play."""
        row, column = self.ALL_MOVES[self.test_index][self.board.motif_count]
        self.board.update(player, row, column)
        self.turn += 1
