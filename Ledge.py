from Game import Game
import numpy as np
import copy as cp

class Ledge(Game):
    def __init__(self, board):
        self.initial_state = board
        self.state = cp.deepcopy(board)

    def set_initial_game(self):
        self.state = cp.deepcopy(self.initial_state)

    def get_state(self):
        return self.state

    # Get list of possible actions
    def get_actions(self, state=None):
        if state == None:
            state = self.state

        actions = list()

        for i, coin in enumerate(state):
            if coin is not 0: # Action can only be on coins
                if i == 0:
                    # If current spot is ledge, add action to remove coin
                    actions.append(("remove", coin, (0,0)))
                else:
                    # For each spot towards the ledge until next coin
                    # Add an action to move coin there
                    for b_i, b_coin in enumerate(reversed(state[0:i])):
                        if b_coin is not 0:
                            break
                        else:
                            actions.append(("move", coin, (i, i - 1 - b_i)))
        return actions

    def _do_action(self, state, action):
        if action[0] == "remove":
            state[0] = 0
        else:
            _, coin_value, move = action
            f, t = move
            state[f] = 0
            state[t] = coin_value
        return state

    # Apply action to state
    def do_action(self, action):
        self.state = self._do_action(self.state, action)
        return self.state

    def _is_final_state(self, state):
        return not (2 in state)

    def is_final_state(self):
        return self._is_final_state(self.state)

    # Get where an action takes you (without really doing action)
    def peek(self, state, action):
        return self._do_action(cp.deepcopy(state), action)
