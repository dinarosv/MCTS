from Environment.Ledge import *
from Environment.NIM import *
from Environment.StateManager import *
from MC import Montecarlo
from Player import *
from Gamesimulator import *

if __name__ == "__main__":
    #game = NIM()
    game = Ledge()

    mystatemanager = Statemanager(game=game)

    mc1 = Montecarlo(M=500)
    mc2 = Montecarlo(M=500)
    player1 = Player(mc1)
    player2 = Player(mc2)

    gamesimulator = Gamesimulator(player1, player2)

