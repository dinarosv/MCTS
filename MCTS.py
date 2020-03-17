from Node import Node
import random
from Agent import Agent

class MCTS(Agent):
    def __init__(self, state_manager, simulations, rollouts):
        super().__init__(state_manager)
        self.root_node = Node(state_manager)
        self.simulations = simulations
        self.rollouts = rollouts

    # Return action that leads to best state after having performed simulations
    def get_action(self, player):
        for _ in range(self.simulations): #Number of simulations
            print("-------new simulation ------------")
            print(self.root_node.visits)
            # Selection
            node, current_player = self.selection(player, self.root_node)
            # Expansion
            node.expand_child_nodes()
            # Leaf evaluation
            for _, leaf in node.children.items():
                value = self.perform_rollout(leaf, current_player)
                #backpropagation
                self.backpropagate(leaf, value)
            
            # TODO: Aren't q_values updated for each action
            #print(self.root_node.q_values)

        # Choose action
        action = self.root_node.get_max_value_action() if player == 0 else self.root_node.get_min_value_action()
        n = self.root_node.get_child(action)

        # Set root node of the new tree
        self.root_node = Node(self.state_manager, n.state)

        return action

    def selection(self, starting_player, start_node):
        node = start_node
        player = starting_player
        while not node.is_leaf_node():
            # Get action following tree policy (choosing highest/lowest value action)
            action = node.get_max_value_action() if player == 0 else node.get_min_value_action()
            node = node.get_child(action)
            player = abs(player - 1)
        return node, player

    def perform_rollout(self, node, player):
        value = 0
        for _ in range(self.rollouts):
            value += self.rollout(node, player)
            node.prune_children()
        return value/self.rollouts

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
