
from src.board import BlackBishop, BlackKing, BlackKnight, BlackPawn, BlackQueen, BlackRook, Player, Move, WhiteBishop, WhiteKing, WhiteKnight, WhitePawn, WhiteQueen, WhiteRook
from src.movements.bishop import get_all_bishop_moves
from src.movements.king import get_all_king_moves
from src.movements.knight import get_all_knight_moves
from src.movements.movements_utils import is_in_first_column, is_in_first_line, is_in_last_column, is_in_last_line
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

def king_is_atacked_by_knight(squares, king_index: int, current_player: Player) -> bool:
    if current_player == 'White':
        piece_that_can_atack = BlackKnight
    else:
        piece_that_can_atack = WhiteKnight 
    possible_knight_moves = get_all_knight_moves(squares, king_index, current_player)
    return any(map(lambda move: squares[move[1]] == piece_that_can_atack, possible_knight_moves))

def king_is_atacked_by_pawn(squares, king_index: int, current_player: Player) -> bool:
    possible_atacks = []
    if current_player == 'White':
        piece_that_can_atack = BlackPawn
        if not is_in_last_line(king_index):
            if not is_in_first_column(king_index):
                possible_atacks.append((king_index + 8) - 1)
            if not is_in_last_column(king_index):
                possible_atacks.append((king_index + 8) + 1)
    else:
        piece_that_can_atack = WhitePawn
        if not is_in_first_line(king_index):
            if not is_in_first_column(king_index):
                possible_atacks.append((king_index - 8) - 1)
            if not is_in_last_column(king_index):
                possible_atacks.append((king_index - 8) + 1)
    return any(map(
        lambda atack_index: squares[atack_index] == piece_that_can_atack, possible_atacks
    ))

def king_is_atacked_by_oponent_king(squares, king_index: int, current_player: Player) -> bool:
    if current_player == 'White':
        piece_that_can_atack = BlackKing
    else:
        piece_that_can_atack = WhiteKing
    possible_atacks = get_all_king_moves(squares, king_index, current_player)
    return any(map(lambda move: squares[move[1]] == piece_that_can_atack, possible_atacks))
