from class_monster import Monster

class Hero:
    def __init__(self, life = 5, potion = 3):
        self.life = life
        self.potion = potion

    
    def hero_attack(self,monster):
        damage = 1
        monster.life -= damage
        if monster.life > 0:
            print(f"Vous avez attaqué un monster, il a perdu {damage} points de vie. Il lui reste {monster.life} .")
        else:
            print("Le monstre est mort, vous avez gagné!")

    def drink_potion(self):
        self.potion -= 1  
        self.life = 5
        print(f"Vous avez bu une potion, il vous reste {self.potion} potion(s). Vous avez récupéré tous vos points de vie.")
