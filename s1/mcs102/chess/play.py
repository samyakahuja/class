import torch
import chess
import chess.svg
from state import State
from train import Net
import time
import traceback
import base64


class Valuator:

    def __init__(self):
        #load saved parameter values
        vals = torch.load("nets/value.pth", map_location=lambda storage, loc: storage)
        
        #Load the model with saved values
        self.model = Net()
        self.model.load_state_dict(vals)

    def __call__(self, s):
        #board state
        brd = s.serialize()[None]
        #value from net for given board
        output = self.model(torch.tensor(brd).float())
        return float(output.data[0][0])


def explore_leaves(s, v):
    ret = []
    #check value of each legal move from given state
    for e in s.edges():
        s.board.push(e)
        ret.append((v(s), e))
        s.board.pop()
    return ret

def computer_move(s, v):

    #select the best move
    move = sorted(explore_leaves(s, v), key=lambda x: x[0], reverse=s.board.turn)
    
    #print 3 best moves
    print("top 3:")
    for i,m in enumerate(move[0:3]):
        print(" ", m)

    #play the best move
    s.board.push(move[0][1])


# Chess Board and Engine
s = State()
v = Valuator()

def to_svg(s):
  return base64.b64encode(chess.svg.board(board=s.board).encode('utf-8')).decode('utf-8')


# Setup Flask
from flask import Flask, Response, request
app = Flask(__name__)

@app.route("/")
def hello():
    board_svg = to_svg(s)
    ret = '<html><head>'
    ret += '<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>'
    ret += '<style>input { font-size: 30px; } button { font-size: 30px; }</style>'
    ret += '</head><body>'
    ret += '<a href="/selfplay">Play vs itself</a><br/>'
    ret += '<img width=600 height=600 src="data:image/svg+xml;base64,%s"></img><br/>' % board_svg
    ret += '<form action="/move"><input id="move" name="move" type="text"></input><input type="submit" value="Move"></form><br/>'
    ret += '<script>$(function() { var input = document.getElementById("move"); console.log("selected"); input.focus(); input.select(); }); </script>'
    return ret


@app.route("/selfplay")
def selfplay():
    s = State()

    ret = '<html><head>'
    # self play
    while not s.board.is_game_over():
        computer_move(s, v)
        ret += '<img width=600 height=600 src="data:image/svg+xml;base64,%s"></img><br/>' % to_svg(s)
    print(s.board.result())

    return ret

@app.route("/move")
def move():
    if not s.board.is_game_over():
        move = request.args.get('move',default="")
        if move is not None and move != "":
            print("human moves", move)
            try:
                s.board.push_san(move)
                computer_move(s, v)
            except Exception:
                traceback.print_exc()
    else:
        print("GAME IS OVER")
    return hello()


if __name__ == "__main__":
    #display(SVG(chess.svg.board(board = s.board)))
    app.run()
