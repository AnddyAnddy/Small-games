from src.tictactoe.game_mechanic.board import Board
from src.tictactoe.game_mechanic.motif import Motif
from src.tictactoe.user_interface.ui_abstract import UI


class Game:
    def __init__(self, ui: UI.__class__, *args, **kwargs):
        self.board = Board()
        self.ui = ui(self.board, *args, **kwargs)

    def _check_game_over(self) -> bool:
        """Return True when the game is over, e.g. it has a winner or there is no more move to play."""
        return self.board.is_fully_filled or self.board.checks()

    @property
    def has_a_winner(self) -> bool:
        """Return True when the game has a winner."""
        return self.board.checks()

    def main_loop(self) -> Motif:
        players = [Motif.CROSS, Motif.CIRCLE]
        while True:
            self.ui.display()
            self.ui.play(players[self.board.motif_count % 2])
            if self._check_game_over():
                break
        if self.has_a_winner:
            winner = players[(self.board.motif_count - 1) % 2]
            self.ui.display_winner(winner)
        else:
            winner = Motif.BLANK
            self.ui.display_draw()
        return winner
