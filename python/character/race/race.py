from abc import ABC
from ..enemy import enemy


class race(enemy, ABC):

    def __init__(self) -> None:
        super().__init__()
