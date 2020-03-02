
class Game:
    def __init__(self):
        self.state = None

    def get_state(self):
        return self.state

    def get_actions(self):
        raise NotImplementedError

    def do_action(self, action):
        raise NotImplementedError

    def is_final_state(self):
        raise NotImplementedError
