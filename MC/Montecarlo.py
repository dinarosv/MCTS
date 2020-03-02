
class Montecarlo:
  def __init__(self, M):
    self.M = M # Number of simulations/rollouts per episode
    self.tree_policy = None
    self.default_policy = None
    raise NotImplementedError()

  def tree_search(self):
    raise NotImplementedError()

  def node_expansion(self):
    raise NotImplementedError()

  def leaf_evaluation(self):
    raise NotImplementedError()

  def backpropagation(self):
    raise NotImplementedError()