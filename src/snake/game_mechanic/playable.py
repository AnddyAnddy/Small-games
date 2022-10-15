from typing import Protocol


class Playable(Protocol):
    def is_dead(self) -> bool:
        ...
