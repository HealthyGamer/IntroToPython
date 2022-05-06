from player import Player
from encounter import Encounter, Result
from random import randrange


class Game(object):
    def __init__(self):
        self.players = dict()
        self.encounters = dict()

    def getPlayer(self, playerId):
        player = self.players.get(playerId)
        if player is not None:
            self.players[playerId] = player
            return player
        else:
            self.players[playerId] = Player(playerId, 0, 2, 10)
            return self.players[playerId]

    def createEncounter(self, playerId):
        encounter = self.encounters.get(playerId)
        print(encounter)
        if encounter is not None:
            return f"""Current Status:
            Player HP: {self.players[playerId].current_hp}
            Mob HP: {encounter.mob.current_hp}"""
        else:
            player = self.getPlayer(playerId)
            self.encounters[playerId] = Encounter(player)
            return "Encounter created!"

    def playerAction(self, playerId):
        encounter = self.encounters.get(playerId)
        if encounter is None:
            self.createEncounter(playerId)
            encounter = self.encounters[playerId]

        result = encounter.playerAction()
        self.players[playerId] = encounter.player

        if result.result == Result.CONTINUE:
            self.encounters[playerId] = encounter
        else:
            self.completeEncounter(playerId)

        return result.text

    def completeEncounter(self, playerId):
        encounter = self.encounters.get(playerId)
        if encounter is not None:
            del self.encounters[playerId]
            return "Player ran away"
        else:
            return "Encounter not found"
