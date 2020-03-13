from Node import Node
import random
from Agent import Agent

class MCTS(Agent):
    def __init__(self, state_manager, simulations, rollout_simulations):
        super().__init__(state_manager)
        self.root_node = Node(state_manager)
        self.simulations = simulations
        self.rollout_simulations = rollout_simulations

    # Return action that leads to best state after having performed simulations
    def get_action(self, player):
        for _ in range(self.simulations): #Number of simulations
            # Selection
            node, current_player = self.selection(player)
            # Expansion
            node.expand_child_nodes()
            # Leaf evaluation and backpropagation
            for _, leaf in node.children.items():
                self.perform_rollouts(leaf, current_player)
            
            # TODO: Isn't q_values updated for each action
            print(self.root_node.q_values)

        # Choose action
        action = self.root_node.get_max_value_action() if player == 1 else self.root_node.get_min_value_action()
        n = self.root_node.get_child(action)

        # Set root node of the new tree
        self.root_node = Node(self.state_manager, n.state)

        return action

    def selection(self, starting_player):
        node = self.root_node
        player = starting_player
        while not node.is_leaf_node():
            # Get action following tree policy (choosing highest/lowest value action)
            action = node.get_max_value_action() if player == 1 else node.get_min_value_action()
            node = node.get_child(action)
            player = abs(player - 1)
        return node, player

    def perform_rollouts(self, node, player):
        for _ in range(self.rollout_simulations):
            value = self.rollout(node, player)
            self.backpropagate(node, value)
            node.prune_children()

    def rollout(self, node, player):
        if node.is_terminal:
            return node.get_reward(player)
        node.expand_child_nodes()
        action = self.behavior_policy(node)
        node = node.get_child(action)
        return self.rollout(node, abs(player - 1))

    def backpropagate(self, node, value):
        node.backpropagate(value)

    def behavior_policy(self, node):
        return random.sample(list(node.children), 1)[0]

    def reset(self):
        self.root_node = Node(self.state_manager)
