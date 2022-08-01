
from array import array
from typing import Optional


Piece = int
EmptySquare = 0
BlackPawn   = ord('p')
BlackBishop = ord('b')
BlackKnight = ord('n')
BlackRook   = ord('r')
BlackQueen  = ord('q')
BlackKing   = ord('k')
WhitePawn   = ord('P')
WhiteBishop = ord('B')
WhiteKnight = ord('N')
WhiteRook   = ord('R')
WhiteQueen  = ord('Q')
WhiteKing   = ord('K')


class Board:
    def __init__(self):
        self.squares: array[Piece] = array('b', [EmptySquare] * 64) 

    @staticmethod
    def construct_initial_board():
        board = Board()
        pieces_str = [
            'R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R', 
            'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P',
            '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0',
            '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0',
            '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0',
            '\0', '\0', '\0', '\0', '\0', '\0', '\0', '\0',
            'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p',
            'r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'
        ]
        pieces = list(map(ord, pieces_str))
        board.squares = array('b', pieces)
        return board
