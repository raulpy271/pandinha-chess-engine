
from array import array
from typing import Optional

from src.utils import decode_ascii_char


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

    def __str__(self):
        board_in_str =  ' | a b c d e f g h\n' 
        board_in_str += ' -----------------'
        current_row = 0
        for i, piece in enumerate(self.squares):
            if i % 8 == 0:
                current_row += 1
                board_in_str += f'\n{current_row}| '
            board_in_str += (decode_ascii_char(piece) + ' ')
        return board_in_str

    def _convert_column_to_integer(self, column: str) -> int:
        column = column.lower()
        if column in 'abcdefgh':
            return ord(column) - 97
        else:
            raise Exception('Column isn\'t correct')

    def _get_position_integer(self, position_str: str) -> int:
        column_str, row_str = position_str
        column_int = self._convert_column_to_integer(column_str)
        row_int = int(row_str) - 1
        return (row_int * 8) + column_int

    def get_piece(self, position_str: str) -> int:
        position_int = self._get_position_integer(position_str)
        return self.squares[position_int]
