from Node import Node
import random


class MCTS:
    def __init__(self, state_manager):
        self.state_manager = state_manager
        self.root_node = None
        self.tree_policy = dict()
        self.root_node = Node(state_manager)

    def selection(self, starting_player):
        node = self.root_node
        player = starting_player
        while not node.is_leaf_node():
            action = node.get_max_value_action() if player == 1 else node.get_min_value_action()
            node = node.get_child(action)
            player = abs(player - 1)
        return node, player

    def backpropagate(self, node, value):
        node.backpropagate(value)

    def perform_rollouts(self, node, player):
        for _ in range(4000):  # Swap number for the config-variable of how many simulations to do
            _, value = self.rollout(node, player)
            self.backpropagate(node, value)
            node.prune_children()

    def rollout(self, node, player):
        if node.is_terminal:
            return node, node.get_reward(player)
        node.expand_child_nodes()
        action = self.behavior_policy(node)
        node = node.get_child(action)
        return self.rollout(node, abs(player - 1))

    def get_action(self, player):
        for _ in range(200): #Number of simulations
            node, current_player = self.selection(player)
            node.expand_child_nodes()
            for _, leaf in node.children.items():
                self.perform_rollouts(leaf, current_player)

        if player == 1:
            action = self.root_node.get_max_value_action()
            self.root_node = self.root_node.get_child(action)
            print(f"player {player} did {action}")
            return action
        else:
            action = self.root_node.get_min_value_action()
            print(f"player {player} did {action}")
            self.root_node = self.root_node.get_child(action)
            return action
        # Return action that leads to best state after having performed the rollout

    def behavior_policy(self, node):
        return random.sample(list(node.children), 1)[0]