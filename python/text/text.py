from abc import ABC, abstractmethod
import os
from ..character.player import Player


class Text(ABC):

    def __init__(self, player: Player) -> None:
        super().__init__()
        self.print_text(player)

    @abstractmethod
    def print_text(self, player: Player):
        pass

    @abstractmethod
    def player_decision(self, player: Player):
        pass

    def player_interface(self, player: Player):
        print('=' * 80)
        print(player.get_attributes())
        print('=' * 80)

    def clear(self):
        # if windows -> cls otherwise -> clear
        os.system('cls' if os.name == 'nt' else 'clear')
