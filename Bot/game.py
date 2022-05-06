from player import Player


class Game:
    def __init__(self):
        self.players = {}

    def getPlayer(self, playerId):
        player = self.players.get(playerId)
        if player:
            return player
        else:
            self.players[playerId] = Player(playerId, 0, 1, 10)
            return self.players[playerId]
