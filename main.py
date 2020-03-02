from Environment.Ledge import *
from Environment.NIM import *
from MC import Montecarlo

if __name__ == "__main__":
    #myGameSimulator = NIM()
    myGameSimulator = Ledge()
    myMonteCarlo = Montecarlo(M=500, gamesimulator=myGameSimulator)

