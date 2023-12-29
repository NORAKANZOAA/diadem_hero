from class_hero import Hero

hero = Hero()
monsters = []

def get_diademe():
    pass

def check_game():
    pass

while len(monsters) > 0 and hero.life > 0:
    # Afficher le menu

    # En fonction du choix faire des actions

    # HEROS
    #
    # SI attaquer 
    if player_choice == 1:
    # ALORS attaquer
        hero.hero_attack()
    # SINON SI potion
    elif player_choice == 2:
    # ALORS soigner
        hero.drink_potion()

    # MONSTRE
    #
    # SI monstre healer
        if monster == monster_healer:
    # ALORS SI il se soigne
            if monster_healer.heal():
    #   ALORS soigner
                monster_healer.heal()
    #   SINON attaquer
            elif:
            monster_healer.monster_attack()
    # SINON attaquer directement
        else:
            monster.monster_attack()
    
    pass

print("Le jeu est terminé")
