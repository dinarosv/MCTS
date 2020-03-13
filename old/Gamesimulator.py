from Environment.Statemanager import Statemanager

class Gamesimulator:
    def __init__(self, game, player1, player2, config):
        self.game = game
        self.player_turn_index = 0 if config.starting_player == "player1" else 1
        self.players = [player1, player2]
        self.statistics = dict()

    def run_batch(self, number_of_runs):
        for _ in range(number_of_runs):
            self.game.set_initial_game()
            self.run()
        return self.statistics

    def run(self):
        while not self.game.is_final_state():
            player = self.players[self.player_turn_index]
            player.play_turn(self.game) #Getting anything back here?
            self.player_turn_index = (self.player_turn_index + 1) % len(self.players)
            
            if self.game.is_final_state(): #The player won by its move
                self.statistics[player.name] += 1

        self.statistics["played"] += 1
