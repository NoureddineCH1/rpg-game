import random

class Orc:
    def __init__(self):
        self.degat = random.choice(range(3, 6))
        self.loot = random.choice([2.0, 2.1, 2.2, 2.3, 2.4, 2.5])