from random import randrange

class Mob:
    def __init__(self):
        self.hp = 5
        self.attack = 1
        self.xp = 2

    def do_attack(self):
        return self.attack + randrange(2)

    def take_damage(self, damage):
        self.hp -= damage # self.hp - damage
        return self.hp > 0