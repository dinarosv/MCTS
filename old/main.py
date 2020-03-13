from Environment.Ledge import *
from Environment.NIM import *
from Environment.Statemanager import *
from MC.Montecarlo import Montecarlo
from Player import *
from Gamesimulator import *
from ConfigLoader import get_config

if __name__ == "__main__":

    config = get_config()

    #game = NIM()
    game = Ledge(config.ledge_board_configuration)

    statemanager = Statemanager(game)

    mc = Montecarlo(config.simulations_per_game_move, statemanager)
    player1 = Player(mc, "player1")
    player2 = Player(mc, "player2")

    gamesimulator = Gamesimulator(game, player1, player2, config)
    statistics = gamesimulator.run_batch(config.games_in_batch)

    print(statistics)

