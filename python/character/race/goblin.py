from . import race


class Goblin(race.Race):

    def __init__(self) -> None:
        super().__init__()

    def generate_attributes(self, lvl: int = 1):
        self.new_stats({
            'hp': 7,  # health
            'atk': 2,  # attack
            'armor': 2,  # armour
            'mresistance': 1,  # magic resistance
            'dex': 3,  # dexterity
            'lvl': lvl,  # level
        })
