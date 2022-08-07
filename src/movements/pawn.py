
from src.board import Move, EmptySquare, BlackPieces, Player

def move_white_pawn(squares, piece_index: int) -> list[Move]:
    moves = []
    pawn_in_initial_position = piece_index > 7 and piece_index < 16
    can_move_one_square = squares[piece_index + 8] == EmptySquare
    can_move_two_square = pawn_in_initial_position and can_move_one_square and squares[piece_index + 16] == EmptySquare
    left_side = piece_index + 8 - 1
    right_side = piece_index + 8 + 1
    can_capture_to_left_side = piece_index % 8 != 0 and (squares[left_side] in BlackPieces)
    can_capture_to_right_side = (piece_index + 1) % 8 != 0 and (squares[right_side] in BlackPieces)
    if can_move_one_square:
        moves.append([piece_index, piece_index + 8])
    if can_move_two_square:
        moves.append([piece_index, piece_index + 16])
    if can_capture_to_left_side:
        moves.append([piece_index, left_side])
    if can_capture_to_right_side:
        moves.append([piece_index, right_side])
    return moves

def get_all_pawn_moves(squares, piece_index: int, current_player: Player) -> list[Move]:
    if current_player == 'White':
        return move_white_pawn(squares, piece_index)
    else:
        raise Exception('Not implemented black pawn move')
