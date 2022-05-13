from random import randrange
from datetime import datetime


class Player:
    def __init__(self, id, xp=0, attack=0, hp=0):
        self.id = id
        self.xp = xp
        self.attack = attack
        self.max_hp = hp
        self._current_hp = hp
        self.last_hp_update = datetime.now()

    @property
    def current_hp(self):
        now = datetime.now()
        if self._current_hp < self.max_hp:
            time_passed = now - self.last_hp_update
            hp_change = (time_passed.total_seconds() - 30) * .1
            if hp_change + self._current_hp > self.max_hp:
                self._current_hp = self.max_hp
            else:
                self._current_hp += hp_change

        self.last_hp_update = now
        return self._current_hp

    def do_attack(self) -> int:
        return self.attack + randrange(4)

    def take_damage(self, damage) -> bool:
        self._current_hp -= damage
        if self._current_hp < 0:
            self._current_hp = 0
        return self.is_alive()

    def is_alive(self) -> bool:
        return self._current_hp > 0
