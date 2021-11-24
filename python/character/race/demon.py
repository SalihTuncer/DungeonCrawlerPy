from .race import race


class demon(race):

    def __init__(self) -> None:
        super().__init__()

    def generate_attributes(self, lvl: int = 1):
        self.new_stats({
            'hp': 7,  # health
            'atk': 3,  # attack
            'armor': 1,  # armour
            'mresistance': 1,  # magic resistance
            'dex': 3,  # dexterity
            'lvl': lvl,  # level
        })
