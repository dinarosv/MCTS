
class Statemanager:
  def __init__(self, game): 
    self.game = game
    self.game_stats = []

  def set_initial_game(self):
    self.game.set_initial_game()

  def generate_child_states(self, parent_state):
    return self.game.get_actions()

  def is_winning_state(self, state):
    return self.game.is_winning_state()

  def get_game_stats(self):
    return self.game_stats
