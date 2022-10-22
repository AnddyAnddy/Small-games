from src.snake.game_mechanic.coordinates import Position, Direction
from src.snake.game_mechanic.game import Game
from src.snake.game_mechanic.items.apple import Apple
from src.snake.game_mechanic.items.item_type import ItemType
from src.snake.game_mechanic.items.snake import Snake, InfiniteSnake
from src.snake.game_mechanic.items.wall import Wall
from src.snake.user_interface.drawers.factory.factory_drawer import DrawerFactory


def load_level(game: Game, drawer_factory: DrawerFactory, level_path: str):
    with open(f"./resources/levels/{level_path}") as fp:
        lines = fp.read().splitlines()
        to_draw = set()
        for j, line in enumerate(lines):
            for i, char in enumerate(line):
                char: str
                match char.upper():
                    case 'W':
                        game.board.create(ItemType.WALL, forced_position=Position(i, j))
                        to_draw.add('W')
                    case 'S':
                        snake = Snake(Position(i, j), Direction.RIGHT)
                        game.board.add_player(snake)
                        game.board.add(snake)
                        to_draw.add('S')
                    case 'A':
                        game.board.create(ItemType.APPLE, forced_position=Position(i, j))
                        # game.board.add(Apple.create(Position(i, j)))
                        to_draw.add('A')
                    case 'B':
                        game.board.create(ItemType.SPIDER, forced_position=Position(i, j))
                        to_draw.add('B')

                    case 'I':
                        infinite_snake = InfiniteSnake(Position(i, j), Direction.RIGHT)
                        game.board.add_player(infinite_snake)
                        game.board.add(infinite_snake)
                        to_draw.add('I')

        for elem in to_draw:
            match elem:
                case 'W':
                    drawer_factory.wall_drawer(game)
                case 'S':
                    drawer_factory.snake_drawer(game)
                case 'A':
                    drawer_factory.apple_drawer(game)
                case 'B':
                    drawer_factory.spider_drawer(game)
                case 'I':
                    drawer_factory.infinite_snake_drawer(game)
