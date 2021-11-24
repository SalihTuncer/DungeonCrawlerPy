from character.player import player
from character.race.demon import demon

if __name__ == '__main__':
    p1 = player()
    print(p1.get_attributes())
    e1 = demon()
    print(e1.get_attributes())
