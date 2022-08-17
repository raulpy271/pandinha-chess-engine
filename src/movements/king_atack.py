
from src.board import BlackBishop, BlackQueen, BlackRook, Player, Move, WhiteBishop, WhiteQueen, WhiteRook
from src.movements.bishop import get_all_bishop_moves
from src.movements.rook import get_all_rook_moves


def king_is_atacked_by_rook_or_queen(squares, king_index: int, current_player: Player) -> bool:
    if current_player == 'White':
        pieces_that_can_atack = [BlackRook, BlackQueen]
    else:
        pieces_that_can_atack = [WhiteRook, WhiteQueen]
    possible_rook_moves = get_all_rook_moves(squares, king_index, current_player)
    return any(map(lambda move: squares[move[1]] in pieces_that_can_atack, possible_rook_moves))

def king_is_atacked_by_bishop_or_queen(squares, king_index: int, current_player: Player) -> bool:
    if current_player == 'White':
        pieces_that_can_atack = [BlackBishop, BlackQueen]
    else:
        pieces_that_can_atack = [WhiteBishop, WhiteQueen]
    possible_bishop_moves = get_all_bishop_moves(squares, king_index, current_player)
    return any(map(lambda move: squares[move[1]] in pieces_that_can_atack, possible_bishop_moves))
