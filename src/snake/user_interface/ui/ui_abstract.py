from abc import ABC, abstractmethod

from src.snake.game_mechanic.board import Board
from src.snake.game_mechanic.items.abc_item import Item
from src.snake.game_mechanic.playable import Playable
from src.snake.user_interface.drawers.drawers import Drawers


class UI(ABC):

    def __init__(self, board: Board):
        self.board = board
        self.drawers = Drawers()

    @abstractmethod
    def display(self):
        """Display the game to the user."""
        ...

    def draw_item(self, item: Item):
        ...

    @abstractmethod
    def erase(self, item: Item):
        ...

    @abstractmethod
    def play(self, player: Playable):
        ...

    @abstractmethod
    def refresh(self):
        ...
