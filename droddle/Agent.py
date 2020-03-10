from MCTS import MCTS
from Game import Game


class Agent:
    def __init__(self, state_manager):
        self.state_manager = state_manager
        self.MCTS = MCTS(state_manager)

    def get_action(self, player_name):
        return self.MCTS.get_action(player_name)

    def reset(self):
        self.MCTS = MCTS(self.state_manager)
