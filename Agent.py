
class Agent:
    def __init__(self, MCTS):
        self.MCTS = MCTS

    def get_action(self, player):
        return self.MCTS.get_action(player)

    def reset(self):
        self.MCTS.reset()
