import json

def get_config():
    with open('config.json') as config_file:
        data = json.load(config_file)
    
    return Config(data) 

class Config:
    def __init__(self, data):
        self.NIM_N = data["NIM_N"]
        self.NIM_K = data["NIM_K"]
        self.ledge_board_configuration = data["LedgeBoardConfiguration"]
        self.games_in_batch = data["GamesInBatch"]
        self.simulations_per_game_move = data["SimulationsPerGameMove"]
        self.starting_player = data["StartingPlayer"]