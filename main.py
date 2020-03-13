from Ledge import Ledge
from NIM import NIM
import sys, getopt
from GameManager import GameManager

#ledge = Ledge([1, 1, 1, 0, 0, 2])
#nim = NIM(10, 3) 

def main(argv):
    game_type = None
    board = None
    starting_player = None
    M = 500
    batch_size = 1
    verbose = "0"
    opts, _ = getopt.getopt(argv,"hg:b:s:M:n:v:r:",["game=","board=","starting_player=", "M=", "batch=", "verbose="])
    for opt, arg in opts:
        if opt == '-h':
            print("-g or --game: Type of game. Should be 'ledge' or 'nim'")
            print("-b or --board: Initial board. E.g. for ledge: [0,1,1,2,0] and for nim: [10,2]")
            print("-s or --starting_player: Starting player (not required, default is random). 0 or 1.")
            print("-M or --M: Number of simulations (not required, default is 500)")
            print("-n or --batch: Batch-size (not required, default is 1)")
            print("-v or --verbose: 1 to show play-by-play (default is 0 - off)")
            sys.exit(2)
        elif opt in ("-g", "--game"):
            game_type = arg
        elif opt in ("-b", "--board"):
            board = arg
        elif opt in ("-s", "--starting_player"):
            starting_player = eval(arg) if type(eval(arg)) is int else None
        elif opt in ("-M", "--M"):
            M = eval(arg) if type(eval(arg)) is int else 500
        elif opt in ("-n", "--batch"):
            batch_size = eval(arg) if type(eval(arg)) is int else 1
        elif opt in ("-v", "--verbose"):
            verbose = arg
        elif opt in ("-r", "--rollouts"):
            rollouts = eval(arg) if type(eval(arg)) is int else 1000
    if board and game_type:
        board_as_list = eval(board)
        if type(board_as_list) is list:
            if game_type == "nim":
                game = NIM(board_as_list[0], board_as_list[1])
            elif game_type == "ledge":
                game = Ledge(board_as_list)
            else: 
                print("Error: Not valid game")
                sys.exit(2)
        else:
            print("Error: Incorrect board - should be list")
            sys.exit(2)
    else:
        game = NIM(10, 3)

    print(f"Starting game '{game_type}' with board '{board}', starting-player '{starting_player}', M: '{M}', batch-size: '{batch_size}', verbose: '{verbose}'")

    game_manager = GameManager(game=game, player_turn=starting_player, simulations=M)
    won = game_manager.run_batch(batch_size, verbose)
    print(f"Player won: {won}/{batch_size}")

if __name__ == "__main__":
    main(sys.argv[1:])
