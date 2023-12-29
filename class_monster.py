import random

class Monster:
    def __init__(self, life = 5):
        self.life = life
        self.level = random.randint(1,3)

    def monster_attack (self,hero) :
        hero.life -= 1
        print(f"Le monstre vous a attaqué, vous avez perdu 1 point de vie, il vous en reste {hero.life}.")



    
    

