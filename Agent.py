
class Agent:
    def __init__(self, manager):
        self.state_manager = manager

    def get_action(self, player_name):
        raise NotImplementedError

    def reset(self):
        raise NotImplementedError
