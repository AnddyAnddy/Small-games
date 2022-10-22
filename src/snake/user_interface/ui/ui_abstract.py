from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from src.snake.game_mechanic.tick_handler import TickHandler
from src.snake.user_interface.drawers.drawers import Drawers

if TYPE_CHECKING:
    from src.snake.game_mechanic.board import Board
    from src.snake.game_mechanic.items.abc_item import Item
    from src.snake.game_mechanic.playable import Playable


class UI(ABC):

    def __init__(self, board: Board):
        self.board = board
        self.drawers = Drawers()
        self._tick: TickHandler = TickHandler()

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

    @property
    def ticks(self):
        return self._tick.ticks
