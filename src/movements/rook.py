
from typing import Iterator
import itertools

from src.board import Move, Player, WhitePieces, BlackPieces, MoveGenerator
from src.movements.movements_utils import (
    generate_range_of_moves,
    is_in_first_column,
    is_in_first_line,
    is_in_last_column,
    is_in_last_line)


def generate_forward_rook_moves(squares, rook_index: int, adversary_pieces) -> MoveGenerator:
    return generate_range_of_moves(squares, rook_index, adversary_pieces, is_in_last_line, lambda x: x + 8)

def generate_backward_rook_moves(squares, rook_index: int, adversary_pieces) -> MoveGenerator:
    return generate_range_of_moves(squares, rook_index, adversary_pieces, is_in_first_line, lambda x: x - 8)

def generate_left_rook_moves(squares, rook_index: int, adversary_pieces) -> MoveGenerator:
    return generate_range_of_moves(squares, rook_index, adversary_pieces, is_in_first_column, lambda x: x - 1)

def generate_right_rook_moves(squares, rook_index: int, adversary_pieces) -> MoveGenerator:
    return generate_range_of_moves(squares, rook_index, adversary_pieces, is_in_last_column, lambda x: x + 1)

def get_all_rook_moves(squares, rook_index: int, current_player: Player) -> Iterator[Move]:
    iterators = []
    if current_player == 'White':
        adversary_pieces = BlackPieces
    else:
        adversary_pieces = WhitePieces
    iterators.append(generate_forward_rook_moves(squares, rook_index, adversary_pieces))
    iterators.append(generate_backward_rook_moves(squares, rook_index, adversary_pieces))
    iterators.append(generate_right_rook_moves(squares, rook_index, adversary_pieces))
    iterators.append(generate_left_rook_moves(squares, rook_index, adversary_pieces))
    return itertools.chain.from_iterable(iterators)
