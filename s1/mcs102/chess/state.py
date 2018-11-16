import chess
import numpy as np

class State(object):
    def __init__(self, board = None):
        if board is None:
            self.board = chess.Board()
        else:
            self.board = board

    def edges(self):
        return list(self.board.legal_moves)

    def value(self):
        """
        Neural Net evaluates board positions
        V = -1 for black wins board state
        V = 0 for draw board state
        V = 1 for white wins board state
        """
        pass

    def serialize(self):

        assert self.board.is_valid()

        #board state
        bstate = np.zeros(64, np.uint8)

        for i in range(64):
            p = self.board.piece_at(i)
            if p is not None:
                symbol = {'P':1, 'N':2, 'B':3, 'R':4, 'Q':5, 'K':6,
                          'p':9, 'n':10, 'b':11, 'r':12, 'q':13, 'k':14}[p.symbol()]
                bstate[i] = symbol

        #castle for white
        if self.board.has_queenside_castling_rights(chess.WHITE):
            assert bstate[0] == 4 #check if rook on queenside is present
            bstate[0] = 7
        if self.board.has_kingside_castling_rights(chess.WHITE):
            assert bstate[7] == 4 #check if rook on kingside is present
            bstate[7] == 7

        #castle for black
        if self.board.has_queenside_castling_rights(chess.BLACK):
            assert bstate[56] == 12
            bstate[56] = 15
        if self.board.has_kingside_castling_rights(chess.BLACK):
            assert bstate[63] == 12
            bstate[63] == 15


        if self.board.ep_square is not None:
            assert bstate[self.board.ep_square] == 0
            bstate[self.board.ep_square] = 8

        bstate = bstate.reshape(8,8)


        #320 bit representation for NN from shredder_fen board
        state = np.zeros((5,8,8), np.uint8)

        #columns 0 to 3 to binary
        state[0] = (bstate>>3)&1
        state[1] = (bstate>>2)&1
        state[2] = (bstate>>1)&1
        state[3] = (bstate>>0)&1


        #board.turn returns True when it is white to move
        #put last column as whose turn it is to move
        #1 for white, 0 for black
        state[4] = (self.board.turn * 1.0)

        return state


if __name__ == "__main__":
    state = State()
    #print(state.edges())
