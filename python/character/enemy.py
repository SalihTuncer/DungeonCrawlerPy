from abc import ABC
from . import character


class Enemy(character.Character, ABC):

    def __init__(self) -> None:
        super().__init__()
