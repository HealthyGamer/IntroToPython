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

    def playerAction(self):
        damage = self.player.do_attack()
        mobResult = self.mob.takeDamage(damage)
        if(mobResult):
            mobDamage = self.mob.do_attack()
            playerResult = self.player.takeDamage(mobDamage)
            if(playerResult):
                return ActionResult(Result.CONTINUE, f"Player attacked for {damage}. Mob attacked with {mobDamage}.")
            else:
                return ActionResult(Result.LOSE, f"Player attacked for {damage}. Mob attacked with {mobDamage}. Player fainted.")
        else:
            self.grantXP()
            return ActionResult(Result.WIN, f"Player attacked for {damage}. Mob fainted.")

    def grantXP(self):
        self.player.xp += 2
        return self.player
