class Node:
    def __init__(self, state_manager):
        self.state_manager = state_manager
        self.children = dict()
        self.value = 0

    def expand_children(self):
        self.state_manager

    def backpropagate(self, value):
        raise NotImplementedError