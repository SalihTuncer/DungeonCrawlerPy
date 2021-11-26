from .text import Text
from ..character.player import Player


class HometownText(Text):
    def __init__(self, player: Player) -> None:
        super().__init__(player)

    def print_text(self, player: Player):
        print("Welcome to the hometown.")
        print("You have the following options:")
        print("1.Enter the dungeon\n2.Visit the blacksmith\n3.Settings")
        print("Which option do you choose?: ")

    def player_decision(self, player: Player):
        pass
