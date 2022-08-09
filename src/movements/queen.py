
from src.board import Player, Move
from src.movements import bishop, rook


def get_all_queen_moves(squares, queen_index: int, current_player: Player) -> list[Move]:
    moves = []
    moves.extend(bishop.get_all_bishop_moves(squares, queen_index, current_player))
    moves.extend(rook.get_all_rook_moves(squares, queen_index, current_player))
    return moves
