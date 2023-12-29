from class_hero import Hero

hero = Hero()
monsters = []

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

def check_game():


while len(monsters) > 0:
<<<<<<< HEAD
# Afficher le menu
=======
    pass
=======
while True:
>>>>>>> 9e52a96141cf4539b55e34ca3ff25a33c33e278c

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


<<<<<<< HEAD
    # MONSTRE
    #
    # SI monstre healer
    # ALORS SI il se soigne
    #   ALORS soigner
    #   SINON attaquer
    # SINON attaquer directement

=======
    pass
>>>>>>> 9e52a96141cf4539b55e34ca3ff25a33c33e278c
print("Le jeu est terminé")
