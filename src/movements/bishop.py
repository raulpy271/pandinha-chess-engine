
from src.board import Move, Player, WhitePieces, BlackPieces
from src.movements.movements_utils import (
    generate_range_of_moves,
    is_in_first_column,
    is_in_first_line,
    is_in_last_column,
    is_in_last_line)

def generate_primary_diagonal_and_forward_moves(squares, bishop_index: int, adversary_pieces):
    check_boudary = lambda i: is_in_last_line(i) or is_in_last_column(i)
    next_index = lambda i: (i + 8) + 1
    return generate_range_of_moves(squares, bishop_index, adversary_pieces, check_boudary, next_index)

def generate_primary_diagonal_and_backward_moves(squares, bishop_index: int, adversary_pieces):
    check_boudary = lambda i: is_in_first_line(i) or is_in_first_column(i)
    next_index = lambda i: (i - 8) - 1
    return generate_range_of_moves(squares, bishop_index, adversary_pieces, check_boudary, next_index)

def generate_secondary_diagonal_and_forward_moves(squares, bishop_index: int, adversary_pieces):
    check_boudary = lambda i: is_in_last_line(i) or is_in_first_column(i)
    next_index = lambda i: (i + 8) - 1
    return generate_range_of_moves(squares, bishop_index, adversary_pieces, check_boudary, next_index)

def generate_secondary_diagonal_and_backward_moves(squares, bishop_index: int, adversary_pieces):
    check_boudary = lambda i: is_in_first_line(i) or is_in_last_column(i)
    next_index = lambda i: (i - 8) + 1
    return generate_range_of_moves(squares, bishop_index, adversary_pieces, check_boudary, next_index)

def get_all_bishop_moves(squares, bishop_index: int, current_player: Player) -> list[Move]:
    moves = []
    if current_player == 'White':
        adversary_pieces = BlackPieces
    else:
        adversary_pieces = WhitePieces
    moves.extend(generate_primary_diagonal_and_forward_moves(squares, bishop_index, adversary_pieces))
    moves.extend(generate_primary_diagonal_and_backward_moves(squares, bishop_index, adversary_pieces))
    moves.extend(generate_secondary_diagonal_and_forward_moves(squares, bishop_index, adversary_pieces))
    moves.extend(generate_secondary_diagonal_and_backward_moves(squares, bishop_index, adversary_pieces))
    return moves

