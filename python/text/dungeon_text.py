from .text import Text
from ..character.player import Player


class DungeonText(Text):
    def __init__(self, player: Player) -> None:
        super().__init__(player)

    def print_text(self, player: Player):
        print("You entered the deep of the dungeon!")
        print("You have the following options:")
        print("1.Fight\n2.Auto-combat\n3.Open backpack\n4.Escape to the hometown")
        print("Which option do you choose?: ")

    def player_decision(self, player: Player):
        pass
