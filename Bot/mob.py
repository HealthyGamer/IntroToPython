from random import randrange


class Mob:
    def __init__(self):
        self.current_hp = 10
        self.attack = 1
        self.xp = 2

    def do_attack(self):
        return self.attack + randrange(2)

    def take_damage(self, damage):
        self.current_hp -= damage
        return self.is_alive()

    def is_alive(self):
        return self.current_hp > 0
