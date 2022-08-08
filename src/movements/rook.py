
from src.board import Move, EmptySquare, Player, WhitePieces, BlackPieces

def is_in_first_line(index: int) -> bool:
    return index < 8

def is_in_last_line(index: int) -> bool:
    return index >= 8 * 7

def is_in_first_column(index: int) -> bool:
    return index % 8 == 0

def is_in_last_column(index: int) -> bool:
    return (index + 1) % 8 == 0

def generate_range_of_moves(squares, piece_index: int, adversary_pieces, check_boundary, get_next_index) -> list[Move]:
    moves = []
    if check_boundary(piece_index):
        return []
    next_index = get_next_index(piece_index)
    while squares[next_index] == EmptySquare or squares[next_index] in adversary_pieces:
        moves.append([piece_index, next_index])
        if check_boundary(next_index) or squares[next_index] in adversary_pieces: 
            break
        else:
            next_index = get_next_index(next_index)
    return moves

def generate_forward_rook_moves(squares, rook_index: int, adversary_pieces) -> list[Move]:
    return generate_range_of_moves(squares, rook_index, adversary_pieces, is_in_last_line, lambda x: x + 8)

def generate_backward_rook_moves(squares, rook_index: int, adversary_pieces) -> list[Move]:
    return generate_range_of_moves(squares, rook_index, adversary_pieces, is_in_first_line, lambda x: x - 8)

def generate_left_rook_moves(squares, rook_index: int, adversary_pieces) -> list[Move]:
    return generate_range_of_moves(squares, rook_index, adversary_pieces, is_in_first_column, lambda x: x - 1)

def generate_right_rook_moves(squares, rook_index: int, adversary_pieces) -> list[Move]:
    return generate_range_of_moves(squares, rook_index, adversary_pieces, is_in_last_column, lambda x: x + 1)

def get_all_rook_moves(squares, rook_index: int, current_player: Player) -> list[Move]:
    moves = []
    if current_player == 'White':
        adversary_pieces = BlackPieces
    else:
        adversary_pieces = WhitePieces
    moves.extend(generate_forward_rook_moves(squares, rook_index, adversary_pieces))
    moves.extend(generate_backward_rook_moves(squares, rook_index, adversary_pieces))
    moves.extend(generate_right_rook_moves(squares, rook_index, adversary_pieces))
    moves.extend(generate_left_rook_moves(squares, rook_index, adversary_pieces))
    return moves

