
class Gamesimulator:
  def __init__(self, player1, player2, P):
    self.player1 = player1
    self.player2 = player2
    self.P = P # Starting player option

    def run_batch(self, number_of_runs):
        for _ in range(number_of_runs):
            self.run()

    def run(self):
        raise NotImplementedError
