# MCTS
## Project 2: Monte Carlo Tree Search

Run main with flag -h to get the possible options

- -g or --game: Type of game. Should be ledge or nim
- -b or --board: Initial board. E.g. for ledge: [0,1,1,2,0] and for nim: [10,2]
- -s or --starting_player: Starting player (not required, default is random). 0 or 1.
- -M or --M: Number of simulations (not required, default is 500)
- -n or --batch: Batch-size (not required, default is 1)
- -v or --verbose: 1 to show play-by-play (default is 0 - off)


run code (example): python3 main.py -g nim -b [10,3] -v 1