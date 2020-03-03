from Node import Node
import random


class MCTS:
    def __init__(self, state_manager):
        self.state_manager = state_manager
        self.root_node = None

    def select_node(self):
        if self.root_node == None:
            self.root_node = Node(self.state_manager)
            return self.root_node
        else:
            # Propagate to next node to expand on
            raise NotImplementedError

    def backpropagate(self, node, value):
        node.backpropagate(value)

    def perform_rollouts(self, node):
        node.expand_child_nodes()
        for _ in range(50):  # Swap number for the config-variable of how many simulations to do
            # Use behavior policy to pick which node to rollout
            action = self.behavior_policy(node)
            child = node.get_child(action)
            end_node, value = self.rollout(child)
            self.backpropagate(end_node, value)
            child.prune_children()

    def rollout(self, node):
        if node.is_terminal:
            return node, node.get_reward()
        node.expand_child_nodes()
        action = self.behavior_policy(node)
        node = node.get_child(action)
        return self.rollout(node)

    def get_action(self, player_name):
        node = self.select_node()
        self.perform_rollouts(node)
        new_node = self.select_node()
        if player_name == "Protagonist":
            return new_node.get_max_value_action()
        else:
            return new_node.get_min_value_action()
        # Return action that leads to best state after having performed the rollout

    def behavior_policy(self, node):
        return random.sample(node.children, 1)[0]
