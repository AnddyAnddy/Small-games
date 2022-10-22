from abc import ABC, abstractmethod

from src.snake.game_mechanic.game import Game
from src.snake.game_mechanic.items.item_type import ItemType
from src.snake.user_interface.drawers.abc_drawer import Drawer


class DrawerFactory(ABC):
    def add(self, game: Game, item_type: ItemType, drawer: Drawer):
        game.ui.drawers.add(item_type, drawer)

    @abstractmethod
    def apple_drawer(self, game: Game):
        ...

    @abstractmethod
    def wall_drawer(self, game: Game):
        ...

    @abstractmethod
    def snake_drawer(self, game: Game):
        ...

    @abstractmethod
    def spider_drawer(self, game: Game):
        ...

    @abstractmethod
    def infinite_snake_drawer(self, game: Game):
        ...
