from Agent import Agent
from Ledge import Ledge
from NIM import NIM
from GameManager import GameManager
from StateManager import StateManager

game = Ledge([1, 1, 1, 0, 0, 2])
agent = Agent(StateManager(game))

game_manager = GameManager(game, agent)
game_manager.run_batch(200)
