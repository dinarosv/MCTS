
class Game:
    def set_initial_game(self):
        raise NotImplementedError

    def get_state(self):
        raise NotImplementedError

    def get_actions(self):
        raise NotImplementedError

    def do_action(self, action):
        raise NotImplementedError

    def is_final_state(self):
        raise NotImplementedError

