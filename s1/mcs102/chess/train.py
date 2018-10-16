import chess.pgn
from state import State

#reading data from pgn files
with open('data/KingBase2018-A00-A39.pgn') as pgn:
    while 1:
        try:
            game = chess.pgn.read_game(pgn)
        except Exception:
            break

        value = {'1/2-1/2':0, '0-1': -1, '1-0':1}[game.headers["Result"]]
        board = game.board()
        for i, move in enumerate(game.main_line()):
            board.push(move)
            print(value, State(board).serialize())
