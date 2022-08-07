
from src.board import BlackRook, Board, Player, WhitePieces, BlackPieces, Move, EmptySquare, BlackPawn, WhitePawn, WhiteRook
from src.movements import get_all_rook_moves


class Game(Board):
    def __init__(self, player: Player = 'White'):
        super().__init__(player)

    def _get_pieces_of_the_current_player(self) -> list[int]:
        pieces = []
        if self.current_player == 'White':
            is_current_player_piece = lambda piece: piece in WhitePieces
        else:
            is_current_player_piece = lambda piece: piece in BlackPieces
        for i, piece in enumerate(self.squares):
            if is_current_player_piece(piece):
                pieces.append(i)
        return pieces

    def move_white_pawn(self, piece_index: int) -> list[Move]:
        moves = []
        pawn_in_initial_position = piece_index > 7 and piece_index < 16
        can_move_one_square = self.squares[piece_index + 8] == EmptySquare
        can_move_two_square = pawn_in_initial_position and can_move_one_square and self.squares[piece_index + 16] == EmptySquare
        left_side = piece_index + 8 - 1
        right_side = piece_index + 8 + 1
        can_capture_to_left_side = piece_index % 8 != 0 and (self.squares[left_side] in BlackPieces)
        can_capture_to_right_side = (piece_index + 1) % 8 != 0 and (self.squares[right_side] in BlackPieces)
        if can_move_one_square:
            moves.append([piece_index, piece_index + 8])
        if can_move_two_square:
            moves.append([piece_index, piece_index + 16])
        if can_capture_to_left_side:
            moves.append([piece_index, left_side])
        if can_capture_to_right_side:
            moves.append([piece_index, right_side])
        return moves

    def move_pawn(self, piece_index: int) -> list[Move]:
        if self.current_player == 'White':
            return self.move_white_pawn(piece_index)
        else:
            raise Exception('Not implemented black pawn move')

    def get_possible_moves_of_the_pawns(self, pieces_index: list[int]) -> list[Move]:
        moves = []
        pawns_index = filter(
            lambda piece_index: self.squares[piece_index] in [WhitePawn, BlackPawn], 
            pieces_index
        )
        for pawn_index in pawns_index:
            moves.extend(self.move_pawn(pawn_index))
        return moves

    def get_possible_moves_of_the_rooks(self, pieces_index: list[int]) -> list[Move]:
        moves = []
        rooks_index = filter(
            lambda piece_index: self.squares[piece_index] in [BlackRook, WhiteRook], 
            pieces_index
        )
        for rook_index in rooks_index:
            moves.extend(get_all_rook_moves(self.squares, rook_index, self.current_player))
        return moves

    def get_possible_moves(self) -> list[Move]:
        movements = []
        pieces_to_move = self._get_pieces_of_the_current_player()
        movements.extend(
            self.get_possible_moves_of_the_pawns(pieces_to_move)
        )
        movements.extend(
            self.get_possible_moves_of_the_rooks(pieces_to_move)
        )
        return movements
