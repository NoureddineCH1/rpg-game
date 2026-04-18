import random

class Gobelin:
    def __init__(self):
        self.degat = random.choice(range(2, 4))
        self.loot = random.choice([1.0, 1.1, 1.2, 1.3, 1.4, 1.5])