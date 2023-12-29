import random


class Monster:
    def __init__(self, life = 5):
        # self.power = power 
        self.life = life
        self.level = random.randint(1,3)
        # self.monster_attack = int 
    def attack_hero (self,hero) :
        hero.life -= 1

    
    

