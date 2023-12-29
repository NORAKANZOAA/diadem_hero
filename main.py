from class_hero import Hero
from class_monster import Monster
from class_monster_healer import MonsterHealer

hero = Hero()
monster = Monster()

def get_diademe():
    pass

def check_game():
    pass

while monster.life > 0 and hero.life > 0:
    # Afficher le menu

    # En fonction du choix faire des actions

    # HEROS
    #
    # SI attaquer 
    
    # ALORS attaquer
        
    # SINON SI potion
   
    # ALORS soigner
        

    # MONSTRE
    #
    # SI monstre healer
        if isinstance(monster, MonsterHealer):
            # ALORS SI il se soigne
            if monster.heal():
            #   ALORS soigner
                        monster.heal()
            #   SINON attaquer
            else:
                    monster.monster_attack()
            # SINON attaquer directement
        else:
                    monster.monster_attack()
    
        pass

print("Le jeu est terminé")
