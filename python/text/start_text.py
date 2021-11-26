from .text import Text
import re

from ..character.player import Player
from ..exception.name_not_allowed import NameNotAllowed


class StartText(Text):
    def __init__(self, player: Player) -> None:
        super().__init__(player)

    def print_text(self, player: Player):
        print('Welcome to the world of Dungeon Crawler!')
        # now the player is asked for the name of the player
        self.__check_name(player)

    def player_decision(self, player: Player):
        pass

    def __check_name(self, player: Player):
        name = input('What is your name?: ')

        p = re.compile('[a-zA-Z\\s]*')
        try:
            if not p.search(name).group():
                raise NameNotAllowed(name)
        except NameNotAllowed:
            print("Lowercase, uppercase, commas and whitespaces are accepted")
            print("Choose a valid name pls.")
            self.__check_name(player)
            return ''
        print("Hello ", name + ", I will take you to the hometown.")

        player.set_name(name)
