
from typing import Iterator
import itertools

from src.board import Player, Move
from src.movements import bishop, rook


def get_all_queen_moves(squares, queen_index: int, current_player: Player) -> Iterator[Move]:
    bishop_moves_iter = bishop.get_all_bishop_moves(squares, queen_index, current_player)
    rook_moves_iter = rook.get_all_rook_moves(squares, queen_index, current_player)
    return itertools.chain(bishop_moves_iter, rook_moves_iter)
