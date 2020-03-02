from Game import *
import numpy as np


class Ledge(Game):
    def __init__(self, board):
        self.state = board

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


ledge = Ledge([1, 0, 0, 1, 0, 2, 1, 1])
print(ledge.get_actions())
ledge.do_action(("move", 2, (5,4)))
print(ledge.get_actions())