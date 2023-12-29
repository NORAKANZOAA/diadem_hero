from class_hero import Hero
from class_monster import Monster
from class_monster_healer import MonsterHealer

hero = Hero()
monster = Monster()

def show_menu() -> int:
    print("\nC'est à votre tour de jouer, que souhaitez vous faire ?\n")
    print("1 - Attaquer")
    print("2 - Prendre une potion")
    print("3 - Voir les stats")
    print("4 - Quitter le jeu")
    choice = input("\nVotre choix : ")
    if(choice in ("1", "2", "3", "4")):
        return int(choice)
    else:
        show_menu()

def show_menu() -> int:
    print("\nC'est à votre tour de jouer, que souhaitez vous faire ?\n")
    print("1 - Attaquer")
    print("2 - Prendre une potion")
    print("3 - Voir les stats")
    print("4 - Quitter le jeu")
    choice = input("\nVotre choix : ")
    if(choice in ("1", "2", "3", "4")):
        return int(choice)
    else:
        show_menu()

def get_diademe():
    pass

def check_game():
    pass

while True:

    # Show menu to the hero
    choice = show_menu()

    # The hero has chosen a option
    if(choice == 1):
        # The hero attacks
        pass
    elif(choice == 2):
        # The hero wants to take a potion
        if(hero.potion > 0):
            # The hero can take a potion
            pass
        else:
            print("Vous n'avez plus de potion, faîtes un autre choix.")
            continue
    elif(choice == 3):
        # Show stats
        continue
    elif(choice == 4):
        # Quit game
        break
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
