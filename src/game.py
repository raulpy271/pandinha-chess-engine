
from src.board import BlackRook, Board, Player, WhitePieces, BlackPieces, Move, EmptySquare, BlackPawn, WhitePawn, WhiteRook
from src.movements.rook import get_all_rook_moves
from src.movements.pawn import get_all_pawn_moves


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

    def get_possible_moves_of_the_pawns(self, pieces_index: list[int]) -> list[Move]:
        moves = []
        pawns_index = filter(
            lambda piece_index: self.squares[piece_index] in [WhitePawn, BlackPawn], 
            pieces_index
        )
        for pawn_index in pawns_index:
            moves.extend(get_all_pawn_moves(self.squares, pawn_index, self.current_player))
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
