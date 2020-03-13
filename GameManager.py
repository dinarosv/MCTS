from StateManager import StateManager
from Game import Game
from random import randint
from MCTS import MCTS

class GameManager:
    def __init__(self, game, player_turn=None, simulations=500, rollouts=1000):
        self.game = game
        self.state_manager = StateManager(game=game)
        self.agent = MCTS(state_manager=self.state_manager, simulations=simulations, rollout_simulations=rollouts)

        if player_turn == 0 or player_turn == 1:
            self.player_turn = player_turn 
        else:
            self.player_turn = randint(0,1)

    def run(self, verbose):
        while not self.game.is_final_state():
            action = self.agent.get_action(self.player_turn)
            state = self.game.do_action(action)
            if verbose == "1":
                print("------------")
                print(f"player {self.player_turn} did {action}")
                print(f"New state: {state}")
            self.player_turn = abs(self.player_turn - 1)

        if verbose == "1":
            print("------------")
            print(f"Player {self.player_turn} lost!")


    def run_batch(self, batch_size, verbose):
        for _ in range(batch_size):
            if verbose == "1":
                print(f"Starting state: {self.game.get_state()}")

            self.run(verbose)
            self.game.set_initial_game()
            self.agent.reset()
