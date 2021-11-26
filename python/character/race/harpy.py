from . import race


class Harpy(race.Race):

    def __init__(self) -> None:
        super().__init__()

    def generate_attributes(self, lvl: int = 1):
        self.new_stats({
            'hp': 6,  # health
            'atk': 4,  # attack
            'armor': 1,  # armour
            'mresistance': 1,  # magic resistance
            'dex': 3,  # dexterity
            'lvl': lvl,  # level
        })
