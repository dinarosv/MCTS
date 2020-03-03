from Game import Game
import numpy as np
import copy as cp


class Ledge(Game):
    def __init__(self, board):
        self.initial_state = board
        self.state = cp.deepcopy(board)

    def set_initial_game(self):
        self.state = cp.deepcopy(self.initial_state)

    def get_actions(self, state=None):
        if state == None:
            state = self.state

        actions = list()

        for i, coin in enumerate(state):
            if coin is not 0:
                if i == 0:
                    actions.append(("remove", coin))
                else:
                    for b_i, b_coin in enumerate(state[i-1:0:-1]):
                        if b_coin is not 0:
                            break
                        else:
                            actions.append(("move", coin, (i, i-b_i-1)))
        return actions

    def __do_action(self, state, action):
        if action[0] == "remove":
            state[0] = 0
        else:
            _, coin_value, move = action
            f, t = move
            state[f] = 0
            state[t] = coin_value
        return state

    def do_action(self, action):
        self.state = self.__do_action(self.state, action)

    def __is_final_state(self, state):
        return not (1 in state or 2 in state)

    def is_final_state(self):
        return self.__is_final_state(self.state)

    def peek(self, state, action):
        return self.__do_action(action, cp.deepcopy(state))
