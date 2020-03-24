from Game import *
import copy as cp

class NIM(Game):
  def __init__(self, N, K): #N:number of pieces, K: max pieces to remove
    self.N = N
    self.K = K
    self.pieces_left = N

  def set_initial_game(self):
    self.pieces_left = self.N

  def get_state(self):
    return self.pieces_left

  # Get possible actions. Returns list of actions
  def get_actions(self, state=None):
    if state == None:
      state = self.pieces_left
    return [x+1 for x in range(self.K) if x+1 <= state]

  def do_action(self, action):
    self.pieces_left -= action
    if self.pieces_left < 0:
      self.pieces_left = 0
    return self.pieces_left

  def is_final_state(self):
    return self.pieces_left == 0 

  def _do_action(self, state, action):
    state -= action
    if state < 0:
      state = 0
    return state

  def _is_final_state(self, state):
    return state == 0

  # Get where an action takes you (without really doing action)
  def peek(self, state, action):
    return self._do_action(cp.deepcopy(state), action)

