from Environment.Ledge import *
from Environment.NIM import *
from Environment.StateManager import *
from MC import Montecarlo

if __name__ == "__main__":
    #myGameSimulator = NIM()
    myGameSimulator = Ledge()

    mystatemanager = Statemanager(game=myGameSimulator)

    myMonteCarlo = Montecarlo(M=500, statemanager=mystatemanager)

