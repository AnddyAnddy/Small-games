from src.snake.game_mechanic.items.snake import Snake
from src.snake.user_interface.drawers.abc_drawer import Drawer
from src.snake.user_interface.libs import upemtk
from src.tictactoe.user_interface.ui_abstract import UI


class InfiniteSnakeDrawerGraphical(Drawer):
    def __init__(self, ui: UI):
        super().__init__(ui)
        self.optimized_drawer = InfiniteSnakeDrawerGraphical.OptimizedSnakeDrawer(self)

    def draw_head(self, tag, x: int, y: int):
        size = self.ui.case_size
        padding = size // 2
        upemtk.cercle(x * size + padding, y * size + padding, size // 2, remplissage="grey", tag=tag)

    def draw_body(self, tag, x, y):
        size = self.ui.case_size

        ax, ay = x, y
        bx, by = x + 1, y + 1
        upemtk.rectangle(ax * size, ay * size, bx * size, by * size, remplissage='green', tag=tag)

    def draw(self, snake: Snake):
        self.optimized_drawer.draw(snake)

    class OptimizedSnakeDrawer:
        def __init__(self, snake_drawer: "InfiniteSnakeDrawerGraphical"):
            self.snake_drawer = snake_drawer
            self.first_call = False
            self.cursor = None
            self.snake_size = 0

        def draw(self, snake: Snake):
            if not self.first_call:
                self._draw_full_snake(snake, False)
                self.first_call = True
                return
            # detect a change
            if len(snake.body) != self.snake_size:
                self._draw_full_snake(snake, True)
                # erase tail, draw new head and update cursor
            else:
                upemtk.efface(f"{snake.tag}_{self.cursor}")
                x, y = snake.body[0]
                self.snake_drawer.draw_body(f"{snake.tag}_{self.cursor}", x, y)
                self._update_runner(snake)

        def _draw_full_snake(self, snake, erase: bool):
            self.snake_size = len(snake.body)
            for i, (x, y) in enumerate(snake.body):
                i_tag = f"{snake.tag}_{i}"
                if erase:
                    upemtk.efface(i_tag)
                self.snake_drawer.draw_body(i_tag, x, y)
            self.cursor = self.snake_size - 1

        def _update_runner(self, snake):
            self.cursor = self.cursor - 1 if self.cursor != 0 else len(snake.body) - 1
