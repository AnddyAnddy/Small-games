from src.snake.game_mechanic.items.wall import Wall

from src.snake.user_interface.drawers.abc_drawer import Drawer
from src.snake.user_interface.libs import upemtk
from src.tictactoe.user_interface.ui_abstract import UI


class WallDrawerGraphical(Drawer):
    def __init__(self, ui: UI):
        super().__init__(ui)
        self.already_drawn: set[str] = set()

    def draw(self, wall: Wall):
        if wall.tag in self.already_drawn:
            return
        self.already_drawn.add(wall.tag)
        x, y = wall.position
        size = self.ui.case_size
        upemtk.rectangle(x * size, y * size, (x + 1) * size, (y + 1) * size, remplissage="brown", tag=wall.tag)
