import math

class Node:
    def __init__(self, state_manager, state=None, parent=None):
        self.state_manager = state_manager
        self.state = self.state_manager.get_state() if state == None else state
        self.is_terminal = self.state_manager.is_winning_state(self.state)
        self.parent = parent
        self.children = dict()
        self.explorations = dict()
        self.q_values = dict()
        self.accumulated_values = 0
        self.visits = 0
        self.c = 1  # Constant in the exploration formula

    def is_leaf_node(self):
        return len(self.children) == 0

    def expand_child_nodes(self):
        self.visits = 1
        for action, child_state in self.state_manager.generate_child_states(self.state):
            self.explorations[action] = 0
            self.q_values[action] = 0
            self.children[action] = Node(self.state_manager, child_state, self)

    def get_child(self, action):
        return self.children[action]

    def prune_children(self):
        self.children = dict()

    def backpropagate(self, value):
        if self.parent == None:
            return
        action = self.find_causing_action()
        self.parent.explorations[action] += 1 # Should this traversal be counted during backprop? What about rollouts or selection?

        self.parent.accumulated_values += value

        self.parent.q_values[action] = self.parent.accumulated_values / self.parent.explorations[action]
        self.parent.backpropagate(value)

    def get_exploration_bonus(self, action):
        return self.c * math.sqrt(math.log(self.visits) / (1 + self.explorations[action]))

    def get_min_value_action(self):
        values = dict()
        for action in self.children:
            values[action] = self.q_values[action] - self.get_exploration_bonus(action)
        return min(values, key=values.get)

    def get_max_value_action(self):
        values = dict()
        for action in self.children:
            values[action] = self.q_values[action] + self.get_exploration_bonus(action)
        return max(values, key=values.get)

    def find_causing_action(self):
        for action in self.parent.children:
            if self == self.parent.get_child(action):
                return action
        raise RuntimeError

    def get_reward(self, player):
        return 1 if player == 1 else -1