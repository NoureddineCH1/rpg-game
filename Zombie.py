import random

class Zombie:
    def __init__(self):
        self.degat = random.choice(range(1, 3))
        self.loot = random.choice([0.5, 0.6, 0.7, 0.8, 0.9, 1.0])