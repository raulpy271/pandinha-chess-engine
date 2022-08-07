
from src.board import Move, EmptySquare, Player, WhitePieces, BlackPieces

def is_in_first_line(index: int) -> bool:
    return index < 8

def is_in_last_line(index: int) -> bool:
    return index >= 8 * 7

def is_in_first_column(index: int) -> bool:
    return index % 8 == 0

def is_in_last_column(index: int) -> bool:
    return (index + 1) % 8 == 0

def generate_forward_rook_moves(squares, rook_index: int, adversary_pieces) -> list[Move]:
    moves = []
    next_index = rook_index + 8
    while squares[next_index] == EmptySquare or squares[next_index] in adversary_pieces:
        moves.append([rook_index, next_index])
        if is_in_last_line(next_index) or squares[next_index] in adversary_pieces: 
            break
        else:
            next_index += 8
    return moves

def generate_backward_rook_moves(squares, rook_index: int, adversary_pieces) -> list[Move]:
    moves = []
    next_index = rook_index - 8
    while squares[next_index] == EmptySquare or squares[next_index] in adversary_pieces:
        moves.append([rook_index, next_index])
        if is_in_first_line(next_index) or squares[next_index] in adversary_pieces:
            break
        else:
            next_index -= 8
    return moves

def generate_left_rook_moves(squares, rook_index: int, adversary_pieces) -> list[Move]:
    moves = []
    next_index = rook_index - 1
    while squares[next_index] == EmptySquare or squares[next_index] in adversary_pieces:
        moves.append([rook_index, next_index])
        if is_in_first_column(next_index) or squares[next_index] in adversary_pieces:
            break
        else:
            next_index -= 1
    return moves

def generate_right_rook_moves(squares, rook_index: int, adversary_pieces) -> list[Move]:
    moves = []
    next_index = rook_index + 1
    while squares[next_index] == EmptySquare or squares[next_index] in adversary_pieces:
        moves.append([rook_index, next_index])
        if is_in_last_column(next_index) or squares[next_index] in adversary_pieces:
            break
        else:
            next_index += 1
    return moves

def get_all_rook_moves(squares, rook_index: int, current_player: Player) -> list[Move]:
    moves = []
    if current_player == 'White':
        adversary_pieces = BlackPieces
    else:
        adversary_pieces = WhitePieces
    if not is_in_last_line(rook_index):
        moves.extend(generate_forward_rook_moves(squares, rook_index, adversary_pieces))
    if not is_in_first_line(rook_index):
        moves.extend(generate_backward_rook_moves(squares, rook_index, adversary_pieces))
    if not is_in_last_column(rook_index):
        moves.extend(generate_right_rook_moves(squares, rook_index, adversary_pieces))
    if not is_in_first_column(rook_index):
        moves.extend(generate_left_rook_moves(squares, rook_index, adversary_pieces))
    return moves

