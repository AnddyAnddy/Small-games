from abc import ABC, abstractmethod

from src.tictactoe.game_mechanic.board import Board
from src.tictactoe.game_mechanic.motif import Motif


class UI(ABC):
    def __init__(self, board: Board):
        self.board = board

    @abstractmethod
    def display(self):
        """Display the game to the user."""
        ...

    @abstractmethod
    def display_winner(self, winner: Motif):
        """Display the winner of the game to the user."""
        ...

    @abstractmethod
    def display_draw(self):
        """Display a draw when the game is over."""
        ...

    @abstractmethod
    def play(self, player):
        """Interact with the user to have his play and updates the board."""
        ...
