from Player import Player

class ComputerPlayer(Player):
    def __init__(self, agent):
        self.agent = agent

    def get_action(self, state):
        print("-------")
        print(state[0])
        action = self.agent.get_action(state[1])
        print(f"Agent does action: {action}")
        return action
    
    def reset(self):
        self.agent.reset()