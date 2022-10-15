from abc import ABC, abstractmethod

from src.snake.game_mechanic.items.abc_item import Item
from src.tictactoe.user_interface.ui_abstract import UI


class Drawer(ABC):
    def __init__(self, ui: UI):
        self.ui = ui

    @abstractmethod
    def draw(self, item: Item):
        ...
