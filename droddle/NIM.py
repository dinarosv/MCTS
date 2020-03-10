from Game import *

class NIM(Game):
  def __init__(self, N, K): #N:number of pieces, K: max pieces to remove
    self.N = N
    self.K = K
    self.pieces_left = N

  def set_initial_game(self):
    self.pieces_left = self.N

  def get_state(self):
    return self.pieces_left

  def get_actions(self):
    return [x+1 for x in range(self.K) if x+1 <= self.pieces_left]

  def do_action(self, action):
    self.pieces_left -= action
    if self.pieces_left < 0:
      self.pieces_left = 0

  def is_final_state(self):
    return self.pieces_left == 0 
