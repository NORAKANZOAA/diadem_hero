from class_monster import Monster
from class_hero import Hero 

class MonsterHealer(Monster):
    def attack(self, hero):
       hero.life -= 1
    
    def healing(self):
        monster.life += 1