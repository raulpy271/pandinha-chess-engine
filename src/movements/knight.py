
from functools import partial

from src.board import Move, Player
from src.movements.movements_utils import is_in_first_column, is_in_first_line, is_in_last_column, is_in_last_line, can_move_to

def generate_left_and_right_moves(knight_index: int) -> list[Move]:
    moves = []
    column_int = knight_index % 8
    if column_int >= 2:
        if is_in_first_line(knight_index):
            moves.append([knight_index, (knight_index + 8) - 2])
        elif is_in_last_line(knight_index):
            moves.append([knight_index, (knight_index - 8) - 2])
        else:
            moves.append([knight_index, (knight_index + 8) - 2])
            moves.append([knight_index, (knight_index - 8) - 2])
    if column_int <= 5:
        if is_in_first_line(knight_index):
            moves.append([knight_index, (knight_index + 8) + 2])
        elif is_in_last_line(knight_index):
            moves.append([knight_index, (knight_index - 8) + 2])
        else:
            moves.append([knight_index, (knight_index + 8) + 2])
            moves.append([knight_index, (knight_index - 8) + 2])
    return moves

def generate_forward_and_backward_moves(knight_index: int) -> list[Move]:
    moves = []
    row_int = knight_index // 8
    if row_int >= 2:
        if is_in_first_column(knight_index):
            moves.append([knight_index, (knight_index - 16) + 1])
        elif is_in_last_column(knight_index):
            moves.append([knight_index, (knight_index - 16) - 1])
        else:
            moves.append([knight_index, (knight_index - 16) + 1])
            moves.append([knight_index, (knight_index - 16) - 1])
    if row_int <= 5:
        if is_in_first_column(knight_index):
            moves.append([knight_index, (knight_index + 16) + 1])
        elif is_in_last_column(knight_index):
            moves.append([knight_index, (knight_index + 16) - 1])
        else:
            moves.append([knight_index, (knight_index + 16) + 1])
            moves.append([knight_index, (knight_index + 16) - 1])
    return moves

def get_all_knight_moves(squares, knight_index: int, current_player: Player) -> list[Move]:
    moves = []
    moves.extend(generate_left_and_right_moves(knight_index))
    moves.extend(generate_forward_and_backward_moves(knight_index))
    can_move_partial_func = partial(can_move_to, squares, current_player)
    moves = list(filter(lambda move: can_move_partial_func(move[1]), moves))
    return moves
