from random import randrange

class Player:
    def __init__(self, id, xp=0, attack=0, hp=0):
        self.id = id
        self.attack = attack
        self.hp = hp
        self.xp = xp

    def do_attack(self):
        return self.attack + randrange(4)

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        return self.hp > 0