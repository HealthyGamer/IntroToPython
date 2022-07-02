from player import Player
from mob import Mob
from enum import Enum

class Result(Enum):
    CONTINUE = 1
    WIN = 2
    LOSE = 3


class ActionResult:
    def __init__(self, result, text):
        self.result = result
        self.text = text

class Encounter:
    def __init__(self, player: Player):
        self.mob = Mob()
        self.player = player

    def attack(self):
        # player to calc attack damage
        damage = self.player.do_attack()
        # mob takes damage
        mob_result = self.mob.take_damage(damage) # mob will take damage and return whether it is alive
        # if mob is still alive
        if mob_result:
            # calcatulate mob damage
            mob_damage = self.mob.do_attack()
            # player takes damage
            player_result = self.player.take_damage(mob_damage)
            # if player health == 0, player losses
            if player_result:
                return ActionResult(Result.CONTINUE, f"Player attacked for {damage}. Mob attacked with {mob_damage}.")
            else: 
                return ActionResult(Result.LOSE, f"Player attacked for {damage}. Mob attacked with {mob_damage}. Player fainted.")
        # if mob dies - player wins
        else:
            return ActionResult(Result.WIN, f"Player attacked for {damage}. Mob fainted.")