from class_monster import Monster

class Hero:
    def __init__(self, life = 5, potion = 3):
        self.life = life
        self.potion = potion

    
    def hero_attack(self,monster):
        monster.life -= 1

    def drink_potion(self):
        self.potion -= 1 and hero.life == 5



    
hero = Hero(life = 5, potion = 3)
monster = Monster