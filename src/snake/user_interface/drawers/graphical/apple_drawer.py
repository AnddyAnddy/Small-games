from src.snake.game_mechanic.items.apple import Apple

from src.snake.user_interface.drawers.abc_drawer import Drawer
from src.snake.user_interface.libs import upemtk
from src.tictactoe.user_interface.ui_abstract import UI


class AppleDrawerGraphical(Drawer):
    def __init__(self, ui: UI):
        super().__init__(ui)
        self.already_drawn: set[str] = set()

    def draw(self, apple: Apple):
        if apple.tag in self.already_drawn:
            return
        self.already_drawn.add(apple.tag)
        x, y = apple.position
        size = self.ui.case_size
        padding = size // 2
        upemtk.cercle(x * size + padding, y * size + padding, size // 2, remplissage="red", tag=apple.tag)
