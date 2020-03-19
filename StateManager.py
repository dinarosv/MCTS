class StateManager:
    def __init__(self, game):
        self.game = game

    def set_initial_game(self):
        self.game.set_initial_game()

    def get_state(self):
        return self.game.get_state()

    def generate_child_states(self, parent_state):
        children = list()
        actions = self.game.get_actions(parent_state)
        for action in actions:
            child_state = self.game.peek(parent_state, action)
            children.append((action, child_state))
        return children

    def is_winning_state(self, state):
        return self.game._is_final_state(state)

