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
        self.root_node = MCTSNode(self.state_manager, init_player=player)
        for _ in range(self.simulations): #Number of simulations

            # Selection
            node = self.selection()

            # Expansion
            node.expand_child_nodes()

            if node.is_terminal_node():
                leaf = node
            else:
                leaf = node.get_child(self.behavior_policy(node))

            # Leaf evaluation
            winner = self.perform_rollout(leaf)

            #backpropagation
            self.backpropagate(leaf, winner)

        # Choose action
        action = self.root_node.get_most_visited_action()
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
