import math


class Node:
    def __init__(self, state_manager, state=None, parent=None):
        self.state_manager = state_manager
        self.state = self.state_manager.get_state() if state == None else state
        self.is_terimal = self.state_manager.is_winning_state(self.state)
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
        for child_state, action in self.state_manager.expand_child_states():
            self.children[action] = Node(self.state_manager, child_state, self)

    def get_child(self, action):
        self.explorations[(self.state, action)] += 1
        child = self.__get_child(action)
        child.visits += 1
        return child

    def __get_child(self, action):
        return self.children[action]

    def prune_children(self):
        self.children = dict()

    def backpropagate(self, value):
        if self.parent == None:
            return
        action = self.find_causing_action()
        self.parent.explorations[(self.parent.state, action)] += 1
        self.parent.accumulated_values += value
        self.parent.q_values[action] = self.parent.accumulated_values / \
            self.parent.explorations[action]
        self.parent.backpropagate(value)

    def get_exploration_bonus(self, action):
        return self.c * math.sqrt(math.log(self.visits) / (1 + self.explorations[action]))

    def get_q_value(self, action):
        return self.q_values[action]

    def get_min_value_action(self):
        values = dict()
        for action in self.children:
            values[action] = self.q_values[action] - self.explorations[action]
        return min(values, key=values.get)

    def get_max_value_action(self):
        values = dict()
        for action in self.children:
            values[action] = self.q_values[action] + self.explorations[action]
        return max(values, key=values.get)

    def find_causing_action(self):
        for action in self.parent.children:
            if self == self.parent.__get_child(action):
                return action
            else:
                raise RuntimeError  # Failed to find what caused the child to be picked
