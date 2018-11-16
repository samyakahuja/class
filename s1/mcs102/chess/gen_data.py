import chess.pgn
from state import State
import numpy as np

def get_dataset(num_samples = None):
    #reading data from 1 pgn file
    gameCounter = 0
    X,Y = [],[]
    values = {'1/2-1/2':0, '0-1': -1, '1-0':1}
    with open('data/KingBase2018-A00-A39.pgn') as pgn:
        while 1:
            #read each game
            game = chess.pgn.read_game(pgn)
            if game is None:
                break
            
            #in pgn, 1-0 is white won - map it to our value of 1 if white wins.
            res = game.headers['Result']
            if res not in values:
                continue
            value = values[res]

            #init board
            board = game.board()
        
            #iterate through all moves in this game
            for i, move in enumerate(game.main_line()):
                board.push(move)
                enk = State(board).serialize()
                X.append(enk)
                Y.append(value)
            
            print(f"parsing game {gameCounter}\tsamples obtained {len(X)}")

            if num_samples is not None and len(X) > num_samples:
                return X,Y

            gameCounter += 1

    X = np.array(X)
    Y = np.array(Y)
    return X,Y

if __name__ == "__main__":
    X,Y = get_dataset(1e4)
    np.savez('data/dataset.npz', X, Y)
