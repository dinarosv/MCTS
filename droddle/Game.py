
class Game:
    def set_initial_game(self):
        raise NotImplementedError

    def get_state(self):
        raise NotImplementedError

    def get_actions(self):
        raise NotImplementedError

    def do_action(self, action):
        raise NotImplementedError

    def __do_action(self, state, action):
        raise NotImplementedError

    def is_final_state(self):
        raise NotImplementedError

    def __is_final_state(self, state):
        raise NotImplementedError

    def peek(self, state, action):
        raise NotImplementedError
