import random

class Monster:
    def __init__(self, life = 5):
        self.life = life
        self.level = random.randint(1,3)