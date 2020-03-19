from Player import Player

class HumanPlayer(Player):
    def __init__(self):
        pass

    def get_action(self, state):
        print("-------")
        print(state[0])
        print("What is your action?")
        return int(input())