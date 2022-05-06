from random import randrange


class Mob:
    def __init__(self):
        self.current_hp = 10
        self.attack = 1
        self.xp = 2

    def do_attack(self):
        return self.attack + randrange(2)

    def takeDamage(self, damage):
        self.current_hp -= damage
        return self.isAlive()

    def isAlive(self):
        return self.current_hp > 0
