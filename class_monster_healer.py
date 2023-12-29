from class_monster import Monster
from class_hero import Hero 

class MonsterHealer(Monster):
    pass
# qu'est-ce que je dois faire? faire en sorte que le mosntre healer corresponde au monstre de base sauf que selon une certaine probabilité
#il se soigne. 
#dans la fonction attack, il faut qu'il puisse attaquer. Qui? Le hero. Si le hero l'attaque, il perd la moitié de ses vies. 
    def attack(self, hero):
    #le hero attaque puis le monstre attaque; lorsque le hero attaque, le monstre aura 1/2 de ses vies.
    #on fait simplement un -1 sur le nombre de vies du heros 
       hero.life -= 1
    
    def healing(self):
        # une vie lui est restituée sur une probabilité donnée 
        monster.life += 1