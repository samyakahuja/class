import torch
import chess
from state import State
from train import Net

class Valuator:

    def __init__(self):
        #load saved parameter values
        vals = torch.load("nets/value.pth", map_location=lambda storage, loc: storage)
        
        #Load the model with saved values
        self.model = Net()
        self.model.load_state_dict(vals)

    def __call__(self, s):
        brd = s.serialize()[None]
        output = self.model(torch.tensor(brd).float())
        return float(output.data[0][0])


def explore_leaves(s, v):
    ret = []
    for e in s.edges():
        s.board.push(e)
        ret.append((v(s), e))
        s.board.pop()
    return ret

if __name__ == "__main__":

    s = State()
    v = Valuator()

    #play chess
    while not s.board.is_game_over():
        #select the best move
        l = sorted(explore_leaves(s, v), key=lambda x: x[0], reverse=s.board.turn)
        move = l[0]
        print(move)

        #play the best move
        s.board.push(move[1])

    #print result
    print(s.board.result())
