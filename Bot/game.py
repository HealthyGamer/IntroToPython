from player import Player
from encounter import Encounter, Result
from random import randrange


class Game(object):
    def __init__(self):
        self.players = dict()
        self.encounters = dict()

    def get_player(self, player_id):
        player = self.players.get(player_id)
        if player is not None:
            return player
        else:
            self.players[player_id] = Player(player_id, 0, 1, 10)
            return self.players[player_id]

    def create_encounter(self, player_id):
        encounter = self.encounters.get(player_id)
        if encounter:
            return f"""Current Status:
            Player HP: {self.players[player_id].current_hp}
            Mob HP: {encounter.mob.current_hp}"""
        else:
            player = self.players[player_id]
            if player.is_alive():
                self.encounters[player_id] = Encounter(player)
                return "Encounter created!"
            else:
                return "Can't start a fight with no health!"

    def player_action(self, player_id):
        encounter = self.encounters.get(player_id)
        if encounter is None:
            new_encounter = self.create_encounter(player_id)
            encounter = self.encounters[player_id]
            if encounter is None:
                return new_encounter

        result = encounter.player_action()
        self.players[player_id] = encounter.player

        if result.result == Result.CONTINUE:
            self.encounters[player_id] = encounter
        else:
            self.complete_encounter(player_id)

        return result.text

    def complete_encounter(self, player_id):
        encounter = self.encounters.get(player_id)
        if encounter:
            del self.encounters[player_id]
            return "Player ran away"
        else:
            return "Encounter not found"
