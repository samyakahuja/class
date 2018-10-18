import chess.pgn
from state import State

#reading data from 1 pgn file
with open('data/KingBase2018-A00-A39.pgn') as pgn:
    while 1:
        #read each game
        try:
            game = chess.pgn.read_game(pgn)
        except Exception:
            break

        #in pgn 1-0 is white won - map it to our value of 1 if white wins.
        value = {'1/2-1/2':0, '0-1': -1, '1-0':1}[game.headers["Result"]]

        #init board
        board = game.board()
        
        #iterate through all moves in this game
        for i, move in enumerate(game.main_line()):
            board.push(move)
            print("move",i," : ", value, State(board).serialize())

        #read only one game
        break
