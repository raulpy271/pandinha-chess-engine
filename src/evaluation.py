
from src.board import BlackBishop, BlackKnight, BlackPawn, BlackQueen, BlackRook, Board, WhiteBishop, WhiteKnight, WhitePawn, WhiteQueen, WhiteRook

def eval(board: Board) -> int:
    return (
        (9 * (board.squares.count(WhiteQueen) - board.squares.count(BlackQueen))) +
        (5 * (board.squares.count(WhiteRook) - board.squares.count(BlackRook))) +
        (3 * (board.squares.count(WhiteBishop) - board.squares.count(BlackBishop))) +
        (3 * (board.squares.count(WhiteKnight) - board.squares.count(BlackKnight))) +
        (1 * (board.squares.count(WhitePawn) - board.squares.count(BlackPawn)))
    )