from player import Player, Mob


class Encounter:
    def __init__(self, player):
        self.id = 0
        self.mob = Mob()
        self.player = player

    def playerAttack(self):
        damage = self.player.attack()
        self.mob.hp -= damage
        if(self.mob.isAlive()):

        else
        end
