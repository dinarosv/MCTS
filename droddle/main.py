from Agent import Agent
from Ledge import Ledge
from NIM import NIM
from GameManager import GameManager
from StateManager import StateManager

ledge = Ledge([1, 1, 1, 0, 0, 2])
nim = NIM(10, 3) 

agent = Agent(StateManager(nim))

game_manager = GameManager(nim, agent)
game_manager.run_batch(1)
