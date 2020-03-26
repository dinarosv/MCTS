import math

#A class representing a node-structure not concerning any evaluation of nodes.
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

#A class inheriting the general node structure above, but adding the complexity of MCTS-logic
class MCTSNode(Node):
    def __init__(self, state_manager, state=None, parent=None, init_player=None):
        super().__init__(state_manager, state, parent)
        if init_player == None:
            self.player_to_move = abs(self.parent.player_to_move - 1)
        else:
            self.player_to_move = init_player
            
        self.visits = 0
        self.results = {0: 0, 1: 0}

    #Returns the win rate of a given player in the state of the node
    def win_rate(self, player):
        if self.visits == 0:
            return math.inf
        return self.results[player] / (self.visits)

    #This is our tree policy, and is based on win ratio and an exploration bonus.
    def get_best_action(self, c=1):
        values = dict()
        for action, child in self.children.items():
            values[action] = math.inf if child.visits == 0 else child.win_rate(self.player_to_move) + c * math.sqrt(math.log(self.visits) / child.visits)
        return max(values, key=values.get)

    #To pick the action to actually do in a state, we pick the action that was picked the most throughout the simulations
    def get_most_visited_action(self):
        values = dict()
        for action, child in self.children.items():
            values[action] = child.visits
        return max(values, key=values.get)

    #Backpropagate recursively the winning player up through the node-hierarchy
    def backpropagate(self, winning_player):
        #We update the statistics to ensure the correct win rate
        self.visits += 1
        self.results[winning_player] += 1
        if self.parent:
            self.parent.backpropagate(winning_player)

    #Calls the state manager to get possible child states from a given state, and initializes child nodes for these states.
    def expand_child_nodes(self):
        for action, child_state in self.state_manager.generate_child_states(self.state):
            self.children[action] = MCTSNode(self.state_manager, child_state, self)
