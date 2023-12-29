class Hero:
    def __init__(self, life = 5, potion = 3):
        self.life = life
        self.potion = potion

    
    def hero_attack(self,monster):
        monster.life -= 1

    def drink_potion(self):
        self.potion -= 1  
        self.life = 5

