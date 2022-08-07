
from array import array
from typing import Literal

from src.utils import decode_ascii_char
from src.fen_parser import parse_piece_placement


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
WhitePieces = (WhitePawn, WhiteBishop, WhiteKnight, WhiteRook, WhiteQueen, WhiteKing)
BlackPieces = (BlackPawn, BlackBishop, BlackKnight, BlackRook, BlackQueen, BlackKing)

Piece = int
Move = list[int, int]
Player = Literal['White', 'Black']
EmptySquare = 0


class Board:
    def __init__(self, player: Player = 'White'):
        self.squares: array[Piece] = array('b', [EmptySquare] * 64) 
        self.current_player: Player = player

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

    @staticmethod
    def construct_board_from_fen_string(fen_string):
        board = Board()
        fen_parts = fen_string.split(' ')
        piece_placement_part = fen_parts[0]
        pieces = parse_piece_placement(piece_placement_part)
        board.squares = array('b', pieces)
        return board

    def construct_move_str(self, move: Move) -> str:
        current_pos_str = self._get_position_str(move[0])
        next_pos_str = self._get_position_str(move[1])
        return current_pos_str + next_pos_str

    def __str__(self):
        board_in_str =  ' | a b c d e f g h\n' 
        board_in_str += ' -----------------'
        current_row = 0
        for i, piece in enumerate(self.squares):
            if i % 8 == 0:
                current_row += 1
                board_in_str += f'\n{current_row}| '
            if piece:
                board_in_str += (decode_ascii_char(piece) + ' ')
            else:
                board_in_str += '  '
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

    def _get_position_str(self, position_int: int) -> str:
        row_int = position_int // 8
        column_int = position_int % 8
        column_str = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'][column_int]
        return f'{column_str}{row_int + 1}'

    def get_piece(self, position_str: str) -> int:
        position_int = self._get_position_integer(position_str)
        return self.squares[position_int]

