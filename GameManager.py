from StateManager import StateManager
from Game import Game
from random import randint
from MCTS import MCTS

class GameManager:
    def __init__(self, game, player_turn=None, simulations=500):
        self.game = game
        self.state_manager = StateManager(game=game)
        if player_turn == 0 or player_turn == 1:
            self.player_turn = player_turn
            self.static_player = True
        else:
            self.player_turn = randint(0,1)
            self.static_player = False
        self.agent = MCTS(state_manager=self.state_manager, simulations=simulations)

    def run(self, verbose):
        turn = self.player_turn
        while not self.game.is_final_state():
            action = self.agent.get_action(turn)
            state = self.game.do_action(action)
            if verbose == "1":
                print("------------")
                print(f"player {turn} did {action}")
                print(f"New state: {state}")
            turn = abs(turn - 1)
        win_turn = abs(turn - 1)
        if verbose == "1":
            print("------------")
            print(f"Player {win_turn} won")
        
        return win_turn


    def run_batch(self, batch_size, verbose):
        win_stats = 0
        for _ in range(batch_size):
            if verbose == "1":
                print(f"Starting state: {self.game.get_state()}")

            win_stats += self.run(verbose)

            self.game.set_initial_game()
            self.player_turn = randint(0,1) if not self.static_player else self.player_turn
        return win_stats
