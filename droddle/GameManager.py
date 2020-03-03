from Agent import Agent
from StateManager import StateManager
from Game import Game


class GameManager:
    def __init__(self, game, agent):
        self.agent = agent
        self.game = game
        self.players = ["Protagonist", "Antagonist"]
        self.player_index = 0  # Make this dependent on config

    def run(self):
        while not self.game.is_final_state():
            player = self.players[self.player_index]

            action = self.agent.get_action(player)
            self.game.do_action(action)

            self.player_index = (self.player_index + 1) % len(self.players)

    def run_batch(self, batch_size):
        for _ in range(batch_size):
            self.run()
