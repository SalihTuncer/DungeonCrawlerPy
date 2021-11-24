from abc import ABC, abstractmethod
from typing import Dict
import random as r


class character(ABC):
    # basic attributes of the Characters in the game
    __attributes = {}
    # equipment
    __equipment = {}

    def __init__(self) -> None:
        self.generate_attributes()

    @abstractmethod
    def generate_attributes(self, lvl: int = 1):
        pass

    def new_stats(self, attributes: Dict[str, int]):
        for key, value in attributes.items():
            if key != "lvl":
                if key in self.__attributes.keys():
                    self.__attributes[key] += int(
                        round(r.random() * value + 1.5))
                else:
                    self.__attributes[key] = int(
                        round(r.random() * value + 1.5))

        self.__attributes['lvl'] = attributes['lvl']
        self.__attributes['xp'] = 0

    def manipulate_attributes(self, changes: Dict[str, int]):
        for key, value in changes.items():
            if key in changes:
                self.__attributes[key] += value

    def is_alive(self):
        return self.hp > 0

    def ready_to_level_up(self):
        return self.__xp >= self.__lvl * 3

    def get_attributes(self):
        return self.__attributes
