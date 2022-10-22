from time import sleep

from src.snake.game_mechanic.board import Board
from src.snake.game_mechanic.coordinates import Direction
from src.snake.game_mechanic.items.abc_item import Item
from src.snake.user_interface.libs import upemtk
from src.snake.user_interface.ui.ui_abstract import UI


def get_direction():
    ev = upemtk.donne_ev()
    tev = upemtk.type_ev(ev)
    match tev:
        case 'Quitte':
            upemtk.ferme_fenetre()
        case 'Touche':
            key = upemtk.touche(ev)
            match key:
                case 'Left':
                    return Direction.LEFT
                case 'Right':
                    return Direction.RIGHT
                case 'Up':
                    return Direction.UP
                case 'Down':
                    return Direction.DOWN
                case 'q':
                    upemtk.ferme_fenetre()
                case 'p':
                    upemtk.attend_ev()
        case _:
            return None


class Graphical(UI):

    def __init__(self, board: Board):
        super().__init__(board)
        self.case_size = 20

    def draw_item(self, item: Item):
        self.drawers.draw(item)

    def display(self):
        self.board.draw(self)
        upemtk.mise_a_jour()

    def erase(self, item: Item):
        upemtk.efface(item.tag)

    def play(self, player: Item):
        direction = get_direction()
        if direction is None:
            return
        player.change_direction(direction)

    def refresh(self):
        sleep(0.2)
        self._tick.update()
