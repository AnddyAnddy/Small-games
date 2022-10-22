from src.snake.game_mechanic.tick_handler import TickHandler
from src.snake.game_mechanic.items.abc_item import Item


def call_frequently(f):
    def inner(*args, **kwargs):
        item: Item = args[0]
        t: TickHandler = TickHandler.instance
        current_tick = t.ticks
        tick_for_item = item.refresh_rate
        if current_tick % tick_for_item == 0:
            return f(*args, **kwargs)
        return None

    return inner

