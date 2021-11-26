from abc import ABC
from .. import enemy


class Race(enemy.Enemy, ABC):

    def __init__(self) -> None:
        super().__init__()
