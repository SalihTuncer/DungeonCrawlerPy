from character.player import player

from character.race.demon import demon
from character.race.goblin import goblin
from character.race.golem import golem
from character.race.harpy import harpy
from character.race.orc import orc
from character.race.troll import troll
from character.race.undead import undead
from character.race.vampire import vampire
import random


if __name__ == '__main__':
    p1 = player()
    print(p1.get_attributes())

    race = random.choice((demon, goblin, golem, harpy,
                         orc, troll, undead, vampire))
    e1 = race()
    print(e1.get_attributes())
    print(type(e1))
