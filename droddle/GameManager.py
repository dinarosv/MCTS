from Agent import Agent
from StateManager import StateManager
from Game import Game


class GameManager:
    def __init__(self, game, agent):
        self.agent = agent
        self.game = game
        self.player_index = 0  # Make this dependent on config

    def run(self):
        while not self.game.is_final_state():
            action = self.agent.get_action(self.player_index)
            self.game.do_action(action)
            self.player_index = abs(self.player_index - 1)

    def run_batch(self, batch_size):
        for _ in range(batch_size):
            self.run()
            self.game.set_initial_game()
            self.agent.reset()
