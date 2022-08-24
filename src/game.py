
from copy import copy
from typing import Iterator
import itertools

from src.logger import logger
from src.board import BlackBishop, BlackKing, BlackKnight, BlackQueen, BlackRook, Board, Piece, Player, WhiteBishop, WhiteKing, WhiteKnight, WhitePieces, BlackPieces, Move, EmptySquare, BlackPawn, WhitePawn, WhiteQueen, WhiteRook, flip_player
from src.movements.rook import get_all_rook_moves
from src.movements.pawn import get_all_pawn_moves
from src.movements.bishop import get_all_bishop_moves
from src.movements.queen import get_all_queen_moves
from src.movements.knight import get_all_knight_moves
from src.movements.king import get_all_king_moves
from src.movements.king_atack import king_is_atacked_by_bishop_or_queen, king_is_atacked_by_knight, king_is_atacked_by_pawn, king_is_atacked_by_rook_or_queen

class Game(Board):
    def __init__(self, player: Player = 'White'):
        super().__init__(player)

    def _get_pieces_of_the_current_player(self) -> list[int]:
        pieces = []
        if self.current_player == 'White':
            is_current_player_piece = lambda piece: piece in WhitePieces
        else:
            is_current_player_piece = lambda piece: piece in BlackPieces
        for i, piece in enumerate(self.squares):
            if is_current_player_piece(piece):
                pieces.append(i)
        return pieces

    def get_possible_moves_of_this_piece(self, pieces_type: list[Piece], all_pieces: list[int], function_that_create_movements_of_single_piece) -> Iterator[Move]:
        iterators = []
        pieces_index = filter(
            lambda piece_index: self.squares[piece_index] in pieces_type, 
            all_pieces
        )
        for piece_index in pieces_index:
            iterators.append(function_that_create_movements_of_single_piece(self.squares, piece_index, self.current_player))
        return itertools.chain.from_iterable(iterators) 

    def king_is_not_secure(self, king_index: int) -> bool:
        return any([
            king_is_atacked_by_bishop_or_queen(self.squares, king_index, self.current_player),
            king_is_atacked_by_rook_or_queen(self.squares, king_index, self.current_player),
            king_is_atacked_by_knight(self.squares, king_index, self.current_player),
            king_is_atacked_by_pawn(self.squares, king_index, self.current_player)
        ])

    def apply_move(self, move: Move) -> "Game":
        board = Game(self.current_player)
        board.squares = copy(self.squares)
        start_move, end_move = move
        board.squares[end_move] = board.squares[start_move]
        board.squares[start_move] = EmptySquare
        return board

    def execute_move(self, move: Move) -> "Game":
        board = self.apply_move(move)
        board.current_player = flip_player(self.current_player)
        return board

    def filter_movements_which_king_is_secure(self, moves: Iterator[Move]) -> Iterator[Move]:
        def is_secure_move(move):
            board = self.apply_move(move)
            king_index = board._get_king_index()
            return not board.king_is_not_secure(king_index)
        moves = filter(is_secure_move, moves)
        return moves

    def get_possible_moves(self) -> Iterator[Move]:
        iterators = []
        pieces_to_move = self._get_pieces_of_the_current_player()
        iterators.append(
            self.get_possible_moves_of_this_piece([BlackPawn, WhitePawn], pieces_to_move, get_all_pawn_moves)
        )
        iterators.append(
            self.get_possible_moves_of_this_piece([BlackRook, WhiteRook], pieces_to_move, get_all_rook_moves)
        )
        iterators.append(
            self.get_possible_moves_of_this_piece([BlackBishop, WhiteBishop], pieces_to_move, get_all_bishop_moves)
        )
        iterators.append(
            self.get_possible_moves_of_this_piece([BlackQueen, WhiteQueen], pieces_to_move, get_all_queen_moves)
        )
        iterators.append(
            self.get_possible_moves_of_this_piece([BlackKnight, WhiteKnight], pieces_to_move, get_all_knight_moves)
        )
        iterators.append(
            self.get_possible_moves_of_this_piece([BlackKing, WhiteKing], pieces_to_move, get_all_king_moves)
        )
        movements_iterators = itertools.chain.from_iterable(iterators)
        return self.filter_movements_which_king_is_secure(movements_iterators)
