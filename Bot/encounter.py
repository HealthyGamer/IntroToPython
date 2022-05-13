from mob import Mob
from player import Player
from enum import Enum


class Result(Enum):
    CONTINUE = 1
    WIN = 2
    LOSE = 3


class ActionResult:

    def __init__(self, result: Result, text: str):
        self.result = result
        self.text = text


class Encounter:
    def __init__(self, player: Player):
        self.id = 0
        self.mob = Mob()
        self.player = player

    def player_action(self):
        damage = self.player.do_attack()
        mob_result = self.mob.take_damage(damage)
        if(mob_result):
            mob_damage = self.mob.do_attack()
            player_result = self.player.take_damage(mob_damage)
            if(player_result):
                return ActionResult(Result.CONTINUE, f"Player attacked for {damage}. Mob attacked with {mob_damage}.")
            else:
                return ActionResult(Result.LOSE, f"Player attacked for {damage}. Mob attacked with {mob_damage}. Player fainted.")
        else:
            self.grant_XP()
            return ActionResult(Result.WIN, f"Player attacked for {damage}. Mob fainted.")

    def grant_XP(self):
        self.player.xp += 2
        return self.player
