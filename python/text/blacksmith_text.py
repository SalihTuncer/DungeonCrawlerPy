from .text import Text
from ..character.player import Player


class BlacksmithText(Text):
    def __init__(self, player: Player) -> None:
        super().__init__(player)

    def print_text(self, player: Player):
        print("You are now at the blacksmith!")
        print("You have the following options:")
        print("1.Forge equipment\n2.Sell equipment\n3.Upgrade equipment\n4.Buy flasks")
        print("5.Return to the hometown")
        print("Which option do you choose?: ")

    def player_decision(self, player: Player):
        pass
