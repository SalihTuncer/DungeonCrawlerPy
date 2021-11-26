from character.player import Player

from character.race.demon import Demon
from character.race.goblin import Goblin
from character.race.golem import Golem
from character.race.harpy import Harpy
from character.race.orc import Orc
from character.race.troll import Troll
from character.race.undead import Undead
from character.race.vampire import Vampire
import random

from python.text.start_text import StartText

if __name__ == '__main__':
    p1 = Player()
    print(p1.get_attributes())

    race = random.choice((Demon, Goblin, Golem, Harpy,
                          Orc, Troll, Undead, Vampire))
    e1 = race()
    print(e1.get_attributes())
    print(type(e1))

    text = StartText(p1)

    print(p1.get_attributes())
