from . import character


class Player(character.Character):

    def __init__(self) -> None:
        super().__init__()

    def generate_attributes(self, lvl: int = 1):
        self.new_stats({
            'hp': 10,  # health
            'atk': 4,  # attack
            'armor': 2,  # armour
            'mresistance': 2,  # magic resistance
            'dex': 2,  # dexterity
            'lvl': lvl,  # level
        })
