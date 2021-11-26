from .text import Text
from ..character.player import Player


class SettingsText(Text):
    def __init__(self, player: Player) -> None:
        super().__init__(player)

    def print_text(self, player: Player):
        print("You are now in the settings:")
        print("You have the following options:")
        print("1.Stats of the player\n2.Stats of the current enemy\n3.Save game\n4.Load game")
        print("5.Quit game\n6.Return")
        print("Which option do you choose?: ")

    def player_decision(self, player: Player):
        pass
