from src.snake.game_mechanic.game import Game
from src.snake.game_mechanic.observers.log_observer import LogObserver
from src.snake.game_mechanic.observers.ui_observer import UIObserver
from src.snake.level import load_level
from src.snake.user_interface.drawers.factory.graphical_factory import GraphicalFactory
from src.snake.user_interface.libs import upemtk
from src.snake.user_interface.ui.ui_graphic import Graphical


def graphical():
    game = Game(Graphical)
    game.attach(UIObserver())
    game.attach(LogObserver())
    load_level(game, GraphicalFactory(), "level1.txt")
    upemtk.cree_fenetre(400, 400)
    game.main_loop()


if __name__ == '__main__':
    graphical()
