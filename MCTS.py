from Node import MCTSNode
import random
from Agent import Agent

class MCTS(Agent):
    def __init__(self, state_manager, simulations, init_player):
        super().__init__(state_manager)
        self.root_node = MCTSNode(state_manager, init_player=init_player)
        self.simulations = simulations
        self.init_player = init_player

    # Return action that leads to best state after having performed simulations
    def get_action(self, player):
        for _ in range(self.simulations): #Number of simulations

            # Selection
            node = self.selection()

            # Expansion
            node.expand_child_nodes()

            if node.is_terminal_node():
                leaf = node
            else:
                leaf = next(iter(node.children.values()))

            # Leaf evaluation
            winner = self.perform_rollout(leaf)

            #backpropagation
            self.backpropagate(leaf, winner)

        # Choose action
        action = self.root_node.get_best_action(c=0)
        n = self.root_node.get_child(action)

        # Set root node of the new tree
        self.root_node = MCTSNode(self.state_manager, state=n.state, init_player=n.player_to_move)

        return action

    def selection(self):
        node = self.root_node
        while not node.is_leaf_node():
            # Get action following tree policy (choosing highest/lowest value action)
            action = node.get_best_action()
            node = node.get_child(action)
        return node

    def perform_rollout(self, node):
        result = self.rollout(node)
        node.prune_children()
        return result

    def rollout(self, node):
        if node.is_terminal_node():
            #The player who made the move to get to this state is the winner
            return abs(node.player_to_move - 1)
        node.expand_child_nodes()
        action = self.behavior_policy(node)
        node = node.get_child(action)
        return self.rollout(node)

    def backpropagate(self, node, value):
        node.backpropagate(value)

    def behavior_policy(self, node):
        return random.sample(list(node.children), 1)[0]

    def reset(self):
        self.root_node = MCTSNode(self.state_manager, init_player=self.init_player)
