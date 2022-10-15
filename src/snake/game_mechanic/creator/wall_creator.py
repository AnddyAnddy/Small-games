from random import randrange
from src.snake.game_mechanic.coordinates import Position, Coordinates
from src.snake.game_mechanic.items.wall import Wall


class WallFactory:
    def __init__(self):
        self.count = 0

    def create(self, available_positions: list[Coordinates] = None, forced_position: Position | None = None) -> Wall:
        if forced_position:
            position = forced_position
        else:
            x = randrange(1, 15)
            y = randrange(1, 15)
            position = Position(x, y)
        self.count += 1
        return Wall(position, f"wall_{self.count}")
