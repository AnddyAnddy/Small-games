from src.snake.game_mechanic.game import Game
from src.snake.game_mechanic.items.item_type import ItemType
from src.snake.user_interface.drawers.factory.factory_drawer import DrawerFactory
from src.snake.user_interface.drawers.graphical.apple_drawer import AppleDrawerGraphical
from src.snake.user_interface.drawers.graphical.infinite_snake_drawer import InfiniteSnakeDrawerGraphical
from src.snake.user_interface.drawers.graphical.snake_drawer import SnakeDrawerGraphical
from src.snake.user_interface.drawers.graphical.spider_drawer import SpiderDrawerGraphical
from src.snake.user_interface.drawers.graphical.wall_drawer import WallDrawerGraphical


class GraphicalFactory(DrawerFactory):
    def apple_drawer(self, game: Game):
        self.add(game, ItemType.APPLE, AppleDrawerGraphical(game.ui))

    def wall_drawer(self, game: Game):
        self.add(game, ItemType.WALL, WallDrawerGraphical(game.ui))

    def snake_drawer(self, game: Game):
        self.add(game, ItemType.SNAKE, SnakeDrawerGraphical(game.ui))

    def infinite_snake_drawer(self, game: Game):
        self.add(game, ItemType.SNAKE, InfiniteSnakeDrawerGraphical(game.ui))

    def spider_drawer(self, game: Game):
        self.add(game, ItemType.SPIDER, SpiderDrawerGraphical(game.ui))
