from .race import race


class undead(race):

    def __init__(self) -> None:
        super().__init__()

    def generate_attributes(self, lvl: int = 1):
        self.new_stats({
            'hp': 8,  # health
            'atk': 2,  # attack
            'armor': 2,  # armour
            'mresistance': 2,  # magic resistance
            'dex': 1,  # dexterity
            'lvl': lvl,  # level
        })
