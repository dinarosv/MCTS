from Environment.Ledge import *
from Environment.NIM import *
from Environment.Statemanager import *
from MC.Montecarlo import Montecarlo
from Player import *
from Gamesimulator import *
from ConfigLoader import get_config

if __name__ == "__main__":

    nim_config, ledge_config, verbose_mode = get_config()

    #game = NIM()
    game = Ledge(ledge_config["BoardConfiguration"])

    mystatemanager = Statemanager(game=game)

    mc1 = Montecarlo(M=500)
    mc2 = Montecarlo(M=500)
    player1 = Player(mc1)
    player2 = Player(mc2)

    gamesimulator = Gamesimulator(player1, player2, statemanager)
    statistics = gamesimulator.run_batch(500)

