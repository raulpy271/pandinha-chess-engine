
from typing import Iterator
from functools import partial

from src.board import Move, Player
from src.movements.movements_utils import (
    is_in_first_column,
    is_in_first_line,
    is_in_last_column,
    is_in_last_line,
    is_free_square)


def get_all_king_moves(squares, king_index: int, current_player: Player) -> Iterator[Move]:
    moves = []
    if is_in_first_column(king_index):
        moves.append([king_index, king_index + 1])
        if is_in_first_line(king_index):
            moves.append([king_index, king_index + 8])
            moves.append([king_index, king_index + 8 + 1])
        elif is_in_last_line(king_index):
            moves.append([king_index, king_index - 8])
            moves.append([king_index, (king_index - 8) + 1])
        else:
            moves.append([king_index, king_index + 8])
            moves.append([king_index, king_index - 8])
            moves.append([king_index, king_index + 8 + 1])
            moves.append([king_index, (king_index - 8) + 1])
    elif is_in_last_column(king_index):
        moves.append([king_index, king_index - 1])
        if is_in_first_line(king_index):
            moves.append([king_index, king_index + 8])
            moves.append([king_index, (king_index + 8) - 1])
        elif is_in_last_line(king_index):
            moves.append([king_index, king_index - 8])
            moves.append([king_index, (king_index - 8) - 1])
        else:
            moves.append([king_index, king_index - 8])
            moves.append([king_index, king_index + 8])
            moves.append([king_index, (king_index + 8) - 1])
            moves.append([king_index, (king_index - 8) - 1])
    else:
        moves.append([king_index, king_index + 1])
        moves.append([king_index, king_index - 1])
        if is_in_first_line(king_index):
            moves.append([king_index, king_index + 8])
            moves.append([king_index, (king_index + 8) + 1])
            moves.append([king_index, (king_index + 8) - 1])
        elif is_in_last_line(king_index):
            moves.append([king_index, king_index - 8])
            moves.append([king_index, (king_index - 8) + 1])
            moves.append([king_index, (king_index - 8) - 1])
        else:
            moves.append([king_index, king_index + 8])
            moves.append([king_index, (king_index + 8) + 1])
            moves.append([king_index, (king_index + 8) - 1])
            moves.append([king_index, king_index - 8])
            moves.append([king_index, (king_index - 8) + 1])
            moves.append([king_index, (king_index - 8) - 1])
    can_move_partial_func = partial(is_free_square, squares, current_player)
    moves = list(filter(lambda move: can_move_partial_func(move[1]), moves))
    return iter(moves)
