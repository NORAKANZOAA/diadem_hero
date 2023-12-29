from class_monster import Monster

class MonsterHealer(Monster):
    def heal(self):
        self.life += 1
        print(f"Le monstre healer s'est soigné et il a {self.life} points de vie.")