from Environment.Game import Game
import numpy as np
import copy as cp

class Ledge(Game):
    def __init__(self, board):
        self.initial_state = board
        self.state = cp.deepcopy(board)

    def set_initial_game(self):
        self.state = cp.deepcopy(self.initial_state)

    def get_actions(self):
        actions = list()

        for i, coin in enumerate(self.state):
            if coin is not 0:
                if i == 0:
                    actions.append(("remove", coin))
                else:
                    for b_i, b_coin in enumerate(self.state[i-1:0:-1]):
                        if b_coin is not 0:
                            break
                        else:
                            actions.append(("move", coin, (i, i-b_i-1)))
        return actions

    def do_action(self, action):
          if action[0] == "remove":
                self.state[0] = 0
          else:
                _, coin_value, move = action
                f, t = move
                self.state[f] = 0
                self.state[t] = coin_value                
            

    def is_final_state(self):
        return not (1 in self.state or 2 in self.state)