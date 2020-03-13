
class Montecarlo:
  def __init__(self, M, state_manager):
    self.M = M # Number of simulations/rollouts per episode
    self.state_manager = state_manager
    self.tree_policy = None
    self.default_policy = None
    raise NotImplementedError()

  def tree_search(self):
    raise NotImplementedError()

  def node_expansion(self):
        child_states = self.state_manager.generate_child_states()

  def leaf_evaluation(self):
    raise NotImplementedError()

  def backpropagation(self):
    raise NotImplementedError()