
class Gamesimulator:
    def __init__(self, player1, player2, statemanager):
        self.player1 = player1
        self.player2 = player2

    def run_batch(self, number_of_runs):
        for _ in range(number_of_runs):
            self.run()

    def run(self):
        raise NotImplementedError
