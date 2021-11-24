from abc import ABC
from .character import character


class enemy(character, ABC):

    def __init__(self) -> None:
        super().__init__()
