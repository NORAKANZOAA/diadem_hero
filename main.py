import random
from class_hero import Hero
from class_monster import Monster
from class_monster_healer import MonsterHealer

hero = Hero()
monster = MonsterHealer()

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


while True:
    if monster.life <= 0:
        break
    if hero.life <= 0:
        print("Vous avez perdu, le monstre vous a tué.")
        break

    # HERO TURN
    choice = show_menu()
   
    if choice == 1:
        hero.hero_attack(monster)
        
        
            
    elif choice == 2:
        if hero.potion > 0:
                hero.drink_potion()
        else:
                print("Vous n'avez plus de potion, faîtes un autre choix.")
        
    elif choice == 3:
            # Show stats
            continue
    elif choice == 4:
            # Quit game
            break
        
    # MONSTER TURN
    if monster.life > 0:
                
        if isinstance(monster, MonsterHealer):
            if random.choice ([True, False,False]):
                monster.heal()
            else:
                monster.monster_attack(hero)
        else:
            monster.monster_attack(hero)
            
print("Le jeu est terminé")
