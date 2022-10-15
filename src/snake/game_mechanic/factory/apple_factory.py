import random

from src.snake.game_mechanic.coordinates import Position, Coordinates
from src.snake.game_mechanic.items.apple import Apple


class AppleFactory:
    def __init__(self):
        self.count = 0

    def create(self, available_positions: list[Coordinates] = None, forced_position: Position | None = None) -> Apple:
        position = forced_position if forced_position else random.choice(available_positions)
        self.count += 1
        return Apple(position, f"apple_{self.count}")
