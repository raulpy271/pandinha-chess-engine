
from src.board import EmptySquare, MoveGenerator, Player, BlackPieces, WhitePieces

def is_in_first_line(index: int) -> bool:
    return index < 8

def is_in_last_line(index: int) -> bool:
    return index >= 8 * 7

def is_in_first_column(index: int) -> bool:
    return index % 8 == 0

def is_in_last_column(index: int) -> bool:
    return (index + 1) % 8 == 0

def is_in_sevent_line(index: int) -> bool:
    return index >= (8 * 6) and index < (8 * 7)

def is_in_second_line(index: int) -> bool:
    return index >= 8 and index < (8 * 2)

def is_free_square(squares, current_player: Player, index: int) -> bool:
    if current_player == 'White':
        adversary_pieces = BlackPieces
    else:
        adversary_pieces = WhitePieces
    return squares[index] == EmptySquare or squares[index] in adversary_pieces

def generate_range_of_moves(squares, piece_index: int, adversary_pieces, check_boundary, get_next_index) -> MoveGenerator:
    if check_boundary(piece_index):
        return
    next_index = get_next_index(piece_index)
    while squares[next_index] == EmptySquare or squares[next_index] in adversary_pieces:
        yield [piece_index, next_index]
        if check_boundary(next_index) or squares[next_index] in adversary_pieces: 
            break
        else:
            next_index = get_next_index(next_index)
