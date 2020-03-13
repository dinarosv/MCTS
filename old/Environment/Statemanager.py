
class Statemanager:
  def __init__(self, game): 
    self.game = game
    raise NotImplementedError()

  def set_initial_game(self):
    raise NotImplementedError()

  def generate_child_states(self, parent_state):
    raise NotImplementedError()

  def is_winning_state(self, state):
    raise NotImplementedError()

  def get_game_stats(self):
    raise NotImplementedError()
