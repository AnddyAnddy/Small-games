from src.snake.game_mechanic.game import Game
from src.snake.game_mechanic.items.item_type import ItemType
from src.snake.user_interface.drawers.graphical.apple_drawer import AppleDrawerGraphical
from src.snake.user_interface.drawers.factory.factory_drawer import DrawerFactory
from src.snake.user_interface.drawers.graphical.snake_drawer import SnakeDrawerGraphical
from src.snake.user_interface.drawers.graphical.wall_drawer import WallDrawerGraphical


class GraphicalFactory(DrawerFactory):
    def apple_drawer(self, game: Game):
        self.add(game, ItemType.APPLE, AppleDrawerGraphical(game.ui))

    def wall_drawer(self, game: Game):
        self.add(game, ItemType.WALL, WallDrawerGraphical(game.ui))

    def snake_drawer(self, game: Game):
        self.add(game, ItemType.SNAKE, SnakeDrawerGraphical(game.ui))