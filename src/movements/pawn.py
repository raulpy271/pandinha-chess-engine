
from src.board import Move, EmptySquare, BlackPieces, Player, WhitePieces, MoveGenerator, PromotionToKnight, PromotionToQueen
from src.movements.movements_utils import is_in_last_column, is_in_first_column, is_in_second_line, is_in_sevent_line

def move_white_pawn(squares, piece_index: int) -> MoveGenerator:
    pawn_in_initial_position = piece_index > 7 and piece_index < 16
    can_move_one_square = squares[piece_index + 8] == EmptySquare
    can_promote = is_in_sevent_line(piece_index)
    can_move_two_square = pawn_in_initial_position and can_move_one_square and squares[piece_index + 16] == EmptySquare
    left_side = piece_index + 8 - 1
    right_side = piece_index + 8 + 1
    pawn_is_in_first_column = is_in_first_column(piece_index)
    pawn_is_in_last_column = is_in_last_column(piece_index)
    can_capture_to_left_side = not pawn_is_in_first_column and (squares[left_side] in BlackPieces)
    can_capture_to_right_side = not pawn_is_in_last_column and (squares[right_side] in BlackPieces)
    if can_promote:
        if can_move_one_square:
            yield [piece_index, piece_index + 8, PromotionToQueen]
            yield [piece_index, piece_index + 8, PromotionToKnight]
        if can_capture_to_left_side:
            yield [piece_index, left_side, PromotionToQueen]
            yield [piece_index, left_side, PromotionToKnight]
        if can_capture_to_right_side:
            yield [piece_index, right_side, PromotionToQueen]
            yield [piece_index, right_side, PromotionToKnight]
        return
    if can_move_one_square:
        yield [piece_index, piece_index + 8]
    if can_move_two_square:
        yield [piece_index, piece_index + 16]
    if can_capture_to_left_side:
        yield [piece_index, left_side]
    if can_capture_to_right_side:
        yield [piece_index, right_side]

def move_black_pawn(squares, piece_index: int) -> MoveGenerator:
    pawn_in_initial_position = piece_index > 47 and piece_index < 56
    can_move_one_square = squares[piece_index - 8] == EmptySquare
    can_promote = is_in_second_line(piece_index)
    can_move_two_square = pawn_in_initial_position and can_move_one_square and squares[piece_index - 16] == EmptySquare
    left_side = (piece_index - 8) - 1
    right_side = (piece_index - 8) + 1
    pawn_is_in_first_column = is_in_first_column(piece_index)
    pawn_is_in_last_column = is_in_last_column(piece_index)
    can_capture_to_left_side = not pawn_is_in_first_column and (squares[left_side] in WhitePieces)
    can_capture_to_right_side = not pawn_is_in_last_column and (squares[right_side] in WhitePieces)
    if can_promote:
        if can_move_one_square:
            yield [piece_index, piece_index - 8, PromotionToQueen]
            yield [piece_index, piece_index - 8, PromotionToKnight]
        if can_capture_to_left_side:
            yield [piece_index, left_side, PromotionToQueen]
            yield [piece_index, left_side, PromotionToKnight]
        if can_capture_to_right_side:
            yield [piece_index, right_side, PromotionToQueen]
            yield [piece_index, right_side, PromotionToKnight]
        return
    if can_move_one_square:
        yield [piece_index, piece_index - 8]
    if can_move_two_square:
        yield [piece_index, piece_index - 16]
    if can_capture_to_left_side:
        yield [piece_index, left_side]
    if can_capture_to_right_side:
        yield [piece_index, right_side]

def get_all_pawn_moves(squares, piece_index: int, current_player: Player) -> MoveGenerator:
    if current_player == 'White':
        return move_white_pawn(squares, piece_index)
    else:
        return move_black_pawn(squares, piece_index)
