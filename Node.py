import math

class Node:
    def __init__(self, state_manager, state=None, parent=None):
        self.state_manager = state_manager
        self.state = self.state_manager.get_state() if state == None else state
        self.parent = parent
        self.children = dict()

    def is_leaf_node(self):
        return len(self.children) == 0
    
    def is_terminal_node(self):
         return self.state_manager.is_winning_state(self.state)

    def get_child(self, action):
        return self.children[action]

    def prune_children(self):
        self.children = dict()


class MCTSNode(Node):
    def __init__(self, state_manager, state=None, parent=None, init_player=None):
        super().__init__(state_manager, state, parent)
        #Fix so that this gets set correctly initially
        if not init_player == None:
            self.player_to_move = init_player
        else:
            self.player_to_move = abs(self.parent.player_to_move - 1)
        self.visits = 0
        self.results = {0: 0, 1: 0}

    def win_rate(self, player):
        return self.results[player] / (self.visits + 1)

    def get_best_action(self, c=1):
        values = dict()
        for action, child in self.children.items():
            values[action] = child.win_rate(self.player_to_move) + c * math.sqrt(math.log(self.visits) / (child.visits + 1))
        return max(values, key=values.get)

    def backpropagate(self, winning_player):
        self.visits += 1
        self.results[winning_player] += 1
        if self.parent:
            self.parent.backpropagate(winning_player)

    def expand_child_nodes(self):
        for action, child_state in self.state_manager.generate_child_states(self.state):
            self.children[action] = MCTSNode(self.state_manager, child_state, self)
