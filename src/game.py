
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

    def _get_pieces_of_the_current_player(self) -> list[int]:
        pieces = []
        if self.current_player == 'White':
            is_current_player_piece = lambda piece: piece in WhitePieces
        else:
            is_current_player_piece = lambda piece: (not (piece in WhitePieces)) and not piece == EmptySquare
        for i, piece in enumerate(self.squares):
            if is_current_player_piece(piece):
                pieces.append(i)
        return pieces

    def get_piece(self, position_str: str) -> int:
        position_int = self._get_position_integer(position_str)
        return self.squares[position_int]

    def move_white_pawn(self, piece_index: int) -> list[Move]:
        moves = []
        pawn_in_initial_position = piece_index > 7 and piece_index < 16
        can_move_one_square = self.squares[piece_index + 8] == EmptySquare
        can_move_two_square = pawn_in_initial_position and can_move_one_square and self.squares[piece_index + 16] == EmptySquare
        if can_move_one_square:
            moves.append([piece_index, piece_index + 8])
        if can_move_two_square:
            moves.append([piece_index, piece_index + 16])
        return moves

    def move_pawn(self, piece_index: int) -> list[Move]:
        if self.current_player == 'White':
            return self.move_white_pawn(piece_index)
        else:
            raise Exception('Not implemented black pawn move')

    def get_possible_moves_of_the_paws(self, pieces_index: list[int]) -> list[Move]:
        moves = []
        pawns_index = filter(
            lambda piece_index: self.squares[piece_index] in [WhitePawn, BlackPawn], 
            pieces_index
        )
        for pawn_index in pawns_index:
            moves.extend(self.move_pawn(pawn_index))
        return moves

    def get_possible_moves(self) -> list[Move]:
        movements = []
        pieces_to_move = self._get_pieces_of_the_current_player()
        movements.extend(
            self.get_possible_moves_of_the_paws(pieces_to_move)
        )
        return movements
