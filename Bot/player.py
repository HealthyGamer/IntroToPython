from random import randrange


class Player:
    def __init__(self, id, xp=0, attack=0, hp=0):
        self.id = id
        self.xp = xp
        self.attack = attack
        self.max_hp = hp
        self.current_hp = hp

    def do_attack(self) -> int:
        return self.attack + randrange(4)

    def takeDamage(self, damage) -> bool:
        self.current_hp -= damage
        return self.isAlive()

    def isAlive(self) -> bool:
        return self.current_hp > 0
