import chess

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
        #257 bit representation for NN
        return self.board.shredder_fen()


if __name__ == "__main__":
    state = State()
    print(state.edges())
