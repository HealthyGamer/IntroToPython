from player import Player
from encounter import Encounter, Result

class Game:

    def __init__(self):
        self.players = {}
        self.encounters = {}

    def get_player(self, player_id):
        player = self.players.get(player_id) #self.players[player_id] throws an error if it's not there
        if player:
            return player
        else:
            self.players[player_id] = Player(player_id, 0, 1, 10)
            return self.players[player_id]

#if we have one for a player, let them know what current status
    def create_encounter(self, player_id):
        encounter = self.encounters.get(player_id)
        if encounter:
            return f"""Current encounter:
            Player HP: {self.players[player_id].hp}
            Mob HP: {encounter.mob.hp}
            """
        else:
            player = self.get_player(player_id)
            self.encounters[player_id] = Encounter(player)
            return "Encounter created."
    
    def attack(self, player_id):
        player = self.get_player(player_id)
        encounter = self.encounters.get(player_id)
        if encounter is None:
            self.encounters[player_id] = Encounter(player)
            encounter = self.encounters[player_id]

        result = encounter.attack()

        if result == Result.CONTINUE: #encounter continues
            #save the data to the "database"
            self.encounters[player_id] = encounter
            self.players[player_id] = encounter.player
        else:
            self.players[player_id] = encounter.player
            self.complete_encounter(player_id)

        return result.text

    def complete_encounter(self, player_id):
        encounter = self.encounters.get(player_id)
        if encounter:
            del self.encounters[player_id]
            return "Player ran away."
        else:
            return "Encounter not found."