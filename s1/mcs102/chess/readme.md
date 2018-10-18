
## Board

Board position notation used is [FEN](https://en.wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation) - record

## DataSet

Data-Set used is from [Kingbase-chess](http://www.kingbase-chess.net/) 2018 Release PNG formatted


## Theory

Every position in chess is either a win for white, a win for black, or draw.
We can denote this by the function `f(position)`.

Now if we had a black box to compute this by:
1. Assign all the final positions value -1,0,1 depending on who wins
2. Use the recursive rule ``` f(p) = max -f(p') ``` for `p -> p'`

Here p -> p' denotes the legal moves from position p. The minus sign is because
the players alternate between positions, the same as minimax.

There is no way to actually compute this black box, so we resort to approximations
that we calculate using machine learning, specifically deep-learning.

## Model

### Input layer

> Input layer will have 8 * 8 * (no_of_pieces) units

This representation is called as *Bitmap Input* which represents all 64 squares
of the board using 12(shown below) binary features plus additional.

Number of pieces: 2 + 14 = 16
bits used: lg(16) = 2

+ for-all : 1 + 1 = 2
    1. blank
    2. blank (En passant)

+ White and Black : 7 * 2 = 14
    1. pawn
    2. knight
    3. bishop
    4. rook
    5. queen
    6. king
    7. castle

+ Extra info: 1 
    1. side to move

> This amounts to **(8 * 8 * 4) + 1 = 257** bits in input vector

Alternative would be to use 8 * 8 * 4 = 768 units in input layer plus
side to move and castling rights.

TODO:
Do we want to include extra information like:
+ White Castle Rights
    + king side
    + queen side
+ Black Castle Rights
    + king side
    + queen side

## Dependencies

+ python-chess
