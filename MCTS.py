from Node import MCTSNode
import random
from Agent import Agent

class MCTS(Agent):
    def __init__(self, state_manager, simulations):
        super().__init__(state_manager)
        self.simulations = simulations
        self.state_manager = state_manager

    # Return action that leads to best state after having performed simulations
    def get_action(self, player):
        #Initialize a new root node with the current game state before the simulations start
        self.root_node = MCTSNode(self.state_manager, init_player=player)
        for _ in range(self.simulations): #Number of simulations

            # Selection
            node = self.selection()

            # Expansion
            node.expand_child_nodes()

            # Find a child to do rollouts on unless it is a terminal node
            if node.is_terminal_node():
                leaf = node
            else:
                leaf = node.get_child(self.behavior_policy(node))

            # Leaf evaluation
            winner = self.evaluate_leaf_node(leaf)

            # Backpropagation
            self.backpropagate(leaf, winner)

        # Choose action
        return self.root_node.get_most_visited_action()

    # Select leaf node to expand
    def selection(self):
        node = self.root_node
        #Keep propagating down towards a leaf node from the root
        while not node.is_leaf_node():
            # Get action following tree policy
            action = node.get_best_action()
            node = node.get_child(action)
        return node

    # Gets the winner of a rollout
    def evaluate_leaf_node(self, node):
        result = self.rollout(node)
        node.prune_children()
        return result

    # Recursive function to get to a terminal node to find a victor
    def rollout(self, node):
        if node.is_terminal_node():
            # The player who made the move to get to this state is the winner
            return abs(node.player_to_move - 1)
        node.expand_child_nodes()
        # Use behavior policy in rollout. For us it is a random choice from children
        action = self.behavior_policy(node)
        node = node.get_child(action)
        return self.rollout(node)

    def backpropagate(self, node, value):
        # Feed the result to the backpropagate-function of the node that the rollout was performed on
        node.backpropagate(value)

    def behavior_policy(self, node):
        # Our behavior policy is random
        return random.sample(list(node.children), 1)[0]
