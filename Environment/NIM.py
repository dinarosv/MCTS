from Environment.Game import *

class NIM(Game):
  def __init__(self, N, K): #N:number of pieces, K: max pieces to remove
    self.N = N
    self.K = K

  def get_state(self):
    return self.N

  def get_actions(self):
    return [x+1 for x in range(self.K) if x+1 <= self.N]

  def do_action(self, action):
    self.N -= action
    if self.N < 0:
      self.N = 0

  def is_final_state(self):
    return self.N == 0 
